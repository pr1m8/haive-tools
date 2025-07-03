"""Type Hints Transformer Module

This module provides functionality to add type hints to function parameters and
return types in Python code using LibCST. It allows for automated type annotation
of existing code to improve type safety and code documentation.

Example:
    >>> import libcst as cst
    >>> from haive.tools.toolkits.dev.python.cst_toolkit.transformers.type_hints import TypeHintTransformer
    >>>
    >>> # Read and parse source code
    >>> with open("script.py", "r") as f:
    >>>     tree = cst.parse_module(f.read())
    >>>
    >>> # Define type mapping
    >>> type_map = {
    >>>     "name": "str",
    >>>     "age": "int",
    >>>     "return": "bool"
    >>> }
    >>>
    >>> # Apply type hints
    >>> modified_tree = tree.visit(TypeHintTransformer(type_map))
    >>>
    >>> # Write updated code back to file
    >>> with open("script.py", "w") as f:
    >>>     f.write(modified_tree.code)
"""

import libcst as cst


class TypeHintTransformer(cst.CSTTransformer):
    """Adds type hints to function parameters and return types.

    This transformer identifies function parameters and adds appropriate
    type annotations based on a provided mapping. It can also add a return
    type annotation to functions.

    Attributes:
        type_map (dict): A dictionary mapping parameter names and 'return' to their types
    """

    def __init__(self, type_map):
        """Initialize the type hint transformer with a mapping of types.

        Args:
            type_map (dict): A dictionary mapping parameter names and 'return' to their
                types, in the format {"param_name": "type", "return": "return_type"}
        """
        super().__init__()
        self.type_map = type_map  # {"param_name": "int", "return": "str"}

    def leave_FunctionDef(self, original_node, updated_node):
        """Add type hints to function definitions during the AST traversal.

        This method adds type annotations to function parameters and return types
        based on the provided type_map.

        Args:
            original_node (cst.FunctionDef): The original function definition node
            updated_node (cst.FunctionDef): The updated function definition node

        Returns:
            cst.FunctionDef: The function definition with added type hints for parameters
                and return type if specified in the type_map
        """
        updated_params = []
        for param in updated_node.params.params:
            param_name = param.name.value
            annotation = self.type_map.get(param_name, None)
            if annotation:
                param = param.with_changes(
                    annotation=cst.Annotation(cst.parse_expression(annotation))
                )
            updated_params.append(param)

        return_annotation = self.type_map.get("return")
        return updated_node.with_changes(
            params=updated_node.params.with_changes(params=updated_params),
            returns=(
                cst.Annotation(cst.parse_expression(return_annotation))
                if return_annotation
                else updated_node.returns
            ),
        )
