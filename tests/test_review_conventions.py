import ast
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parent.parent


def parse_module(path: str) -> ast.Module:
    return ast.parse((ROOT / path).read_text())


def find_function(
    module: ast.Module, name: str
) -> ast.FunctionDef | ast.AsyncFunctionDef:
    for node in module.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name:
            return node
    msg = f"Function {name!r} not found"
    raise AssertionError(msg)


class ReviewConventionTests(unittest.TestCase):
    def test_new_handlers_use_root_names_and_return_annotations(self) -> None:
        cases = {
            "apps/emmett_hello_world.py": ("root", "str"),
            "apps/muffin_hello_world.py": ("root", "str"),
            "apps/responder_hello_world.py": ("root", "None"),
            "apps/connexion_hello_world.py": ("root", "str"),
        }

        for path, (name, return_type) in cases.items():
            with self.subTest(path=path):
                function = find_function(parse_module(path), name)
                self.assertIsNotNone(function.returns)
                self.assertEqual(ast.unparse(function.returns), return_type)

    def test_twisted_get_handler_returns_bytes(self) -> None:
        module = parse_module("apps/twisted_hello_world.py")
        hello_resource = next(
            node
            for node in module.body
            if isinstance(node, ast.ClassDef) and node.name == "HelloResource"
        )
        render_get = next(
            node
            for node in hello_resource.body
            if isinstance(node, ast.FunctionDef) and node.name == "render_GET"
        )

        self.assertIsNotNone(render_get.returns)
        self.assertEqual(ast.unparse(render_get.returns), "bytes")

    def test_connexion_operation_id_points_to_root(self) -> None:
        source = (ROOT / "apps/connexion_hello_world.py").read_text()
        self.assertIn('"operationId": "apps.connexion_hello_world.root"', source)
        self.assertNotIn("tempfile", source)
        self.assertNotIn("mkdtemp", source)
        self.assertIn('"apps.connexion_hello_world:app"', source)

    def test_granian_examples_use_importable_targets(self) -> None:
        cases = {
            "apps/emmett_hello_world.py": '"apps.emmett_hello_world:app"',
            "apps/rsgi_hello_world.py": '"apps.rsgi_hello_world:app"',
        }

        for path, target in cases.items():
            with self.subTest(path=path):
                source = (ROOT / path).read_text()
                self.assertIn(target, source)
                self.assertNotIn('f"{__name__}:app"', source)

    def test_rsgi_app_uses_explicit_protocol_check(self) -> None:
        module = parse_module("apps/rsgi_hello_world.py")
        app = find_function(module, "app")

        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(app)))
        self.assertTrue(any(isinstance(node, ast.If) for node in ast.walk(app)))


if __name__ == "__main__":
    unittest.main()
