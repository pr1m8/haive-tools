
:py:mod:`tools.tools.toolkits.dev.tools`
========================================

.. py:module:: tools.tools.toolkits.dev.tools

Development toolkit for code editing, quality assurance, and Git operations.

This module provides a set of tools for automated code manipulation, including:
- AST-based code transformations (renaming, docstring addition, etc.)
- Code quality checks and automatic fixes
- Git operations and commit management
- Code summarization and analysis

The toolkit uses LibCST for safe, reliable code transformations and provides
a structured interface for common development tasks.

.. rubric:: Examples

>>> from haive.tools.toolkits.dev.tools import CodeEditorTool
>>> editor = CodeEditorTool(debug=True)
>>> config = ASTEditConfig(
...     file_path="/path/to/file.py",
...     edit_type=EditType.ADD_DOCSTRING,
...     target_name="my_function",
...     docstring="This function does something useful."
... )
>>> result = editor.perform_ast_edit(config)
>>> print(result.success)


.. autolink-examples:: tools.tools.toolkits.dev.tools
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.dev.tools.AddDocstringTransformer
   tools.tools.toolkits.dev.tools.AddErrorHandlingTransformer
   tools.tools.toolkits.dev.tools.AddLoggingTransformer
   tools.tools.toolkits.dev.tools.AddParameterTransformer
   tools.tools.toolkits.dev.tools.AddTypeHintsTransformer
   tools.tools.toolkits.dev.tools.ASTEditConfig
   tools.tools.toolkits.dev.tools.BaseTransformer
   tools.tools.toolkits.dev.tools.CodeEditorTool
   tools.tools.toolkits.dev.tools.CodeQualityConfig
   tools.tools.toolkits.dev.tools.CodeQualityTool
   tools.tools.toolkits.dev.tools.CodeStyleConfig
   tools.tools.toolkits.dev.tools.CodeSummarizeConfig
   tools.tools.toolkits.dev.tools.CodeSummary
   tools.tools.toolkits.dev.tools.EditResult
   tools.tools.toolkits.dev.tools.EditType
   tools.tools.toolkits.dev.tools.GitOperation
   tools.tools.toolkits.dev.tools.GitOperationConfig
   tools.tools.toolkits.dev.tools.GitResult
   tools.tools.toolkits.dev.tools.QualityResult
   tools.tools.toolkits.dev.tools.RenameClassTransformer
   tools.tools.toolkits.dev.tools.RenameFunctionTransformer
   tools.tools.toolkits.dev.tools.TransformerContext


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ASTEditConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ASTEditConfig {
        node [shape=record];
        "ASTEditConfig" [label="ASTEditConfig"];
        "pydantic.BaseModel" -> "ASTEditConfig";
      }

.. autopydantic_model:: tools.tools.toolkits.dev.tools.ASTEditConfig
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AddDocstringTransformer:

   .. graphviz::
      :align: center

      digraph inheritance_AddDocstringTransformer {
        node [shape=record];
        "AddDocstringTransformer" [label="AddDocstringTransformer"];
        "BaseTransformer" -> "AddDocstringTransformer";
      }

.. autoclass:: tools.tools.toolkits.dev.tools.AddDocstringTransformer
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AddErrorHandlingTransformer:

   .. graphviz::
      :align: center

      digraph inheritance_AddErrorHandlingTransformer {
        node [shape=record];
        "AddErrorHandlingTransformer" [label="AddErrorHandlingTransformer"];
        "BaseTransformer" -> "AddErrorHandlingTransformer";
      }

.. autoclass:: tools.tools.toolkits.dev.tools.AddErrorHandlingTransformer
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AddLoggingTransformer:

   .. graphviz::
      :align: center

      digraph inheritance_AddLoggingTransformer {
        node [shape=record];
        "AddLoggingTransformer" [label="AddLoggingTransformer"];
        "BaseTransformer" -> "AddLoggingTransformer";
      }

.. autoclass:: tools.tools.toolkits.dev.tools.AddLoggingTransformer
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AddParameterTransformer:

   .. graphviz::
      :align: center

      digraph inheritance_AddParameterTransformer {
        node [shape=record];
        "AddParameterTransformer" [label="AddParameterTransformer"];
        "BaseTransformer" -> "AddParameterTransformer";
      }

.. autoclass:: tools.tools.toolkits.dev.tools.AddParameterTransformer
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AddTypeHintsTransformer:

   .. graphviz::
      :align: center

      digraph inheritance_AddTypeHintsTransformer {
        node [shape=record];
        "AddTypeHintsTransformer" [label="AddTypeHintsTransformer"];
        "BaseTransformer" -> "AddTypeHintsTransformer";
      }

.. autoclass:: tools.tools.toolkits.dev.tools.AddTypeHintsTransformer
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BaseTransformer:

   .. graphviz::
      :align: center

      digraph inheritance_BaseTransformer {
        node [shape=record];
        "BaseTransformer" [label="BaseTransformer"];
        "libcst.CSTTransformer" -> "BaseTransformer";
      }

.. autoclass:: tools.tools.toolkits.dev.tools.BaseTransformer
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CodeEditorTool:

   .. graphviz::
      :align: center

      digraph inheritance_CodeEditorTool {
        node [shape=record];
        "CodeEditorTool" [label="CodeEditorTool"];
      }

.. autoclass:: tools.tools.toolkits.dev.tools.CodeEditorTool
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CodeQualityConfig:

   .. graphviz::
      :align: center

      digraph inheritance_CodeQualityConfig {
        node [shape=record];
        "CodeQualityConfig" [label="CodeQualityConfig"];
        "pydantic.BaseModel" -> "CodeQualityConfig";
      }

.. autopydantic_model:: tools.tools.toolkits.dev.tools.CodeQualityConfig
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CodeQualityTool:

   .. graphviz::
      :align: center

      digraph inheritance_CodeQualityTool {
        node [shape=record];
        "CodeQualityTool" [label="CodeQualityTool"];
        "str" -> "CodeQualityTool";
        "enum.Enum" -> "CodeQualityTool";
      }

.. autoclass:: tools.tools.toolkits.dev.tools.CodeQualityTool
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **CodeQualityTool** is an Enum defined in ``tools.tools.toolkits.dev.tools``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CodeStyleConfig:

   .. graphviz::
      :align: center

      digraph inheritance_CodeStyleConfig {
        node [shape=record];
        "CodeStyleConfig" [label="CodeStyleConfig"];
        "pydantic.BaseModel" -> "CodeStyleConfig";
      }

.. autopydantic_model:: tools.tools.toolkits.dev.tools.CodeStyleConfig
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CodeSummarizeConfig:

   .. graphviz::
      :align: center

      digraph inheritance_CodeSummarizeConfig {
        node [shape=record];
        "CodeSummarizeConfig" [label="CodeSummarizeConfig"];
        "pydantic.BaseModel" -> "CodeSummarizeConfig";
      }

.. autopydantic_model:: tools.tools.toolkits.dev.tools.CodeSummarizeConfig
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CodeSummary:

   .. graphviz::
      :align: center

      digraph inheritance_CodeSummary {
        node [shape=record];
        "CodeSummary" [label="CodeSummary"];
        "pydantic.BaseModel" -> "CodeSummary";
      }

.. autopydantic_model:: tools.tools.toolkits.dev.tools.CodeSummary
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EditResult:

   .. graphviz::
      :align: center

      digraph inheritance_EditResult {
        node [shape=record];
        "EditResult" [label="EditResult"];
        "pydantic.BaseModel" -> "EditResult";
      }

.. autopydantic_model:: tools.tools.toolkits.dev.tools.EditResult
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EditType:

   .. graphviz::
      :align: center

      digraph inheritance_EditType {
        node [shape=record];
        "EditType" [label="EditType"];
        "str" -> "EditType";
        "enum.Enum" -> "EditType";
      }

.. autoclass:: tools.tools.toolkits.dev.tools.EditType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **EditType** is an Enum defined in ``tools.tools.toolkits.dev.tools``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GitOperation:

   .. graphviz::
      :align: center

      digraph inheritance_GitOperation {
        node [shape=record];
        "GitOperation" [label="GitOperation"];
        "str" -> "GitOperation";
        "enum.Enum" -> "GitOperation";
      }

.. autoclass:: tools.tools.toolkits.dev.tools.GitOperation
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GitOperation** is an Enum defined in ``tools.tools.toolkits.dev.tools``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GitOperationConfig:

   .. graphviz::
      :align: center

      digraph inheritance_GitOperationConfig {
        node [shape=record];
        "GitOperationConfig" [label="GitOperationConfig"];
        "pydantic.BaseModel" -> "GitOperationConfig";
      }

.. autopydantic_model:: tools.tools.toolkits.dev.tools.GitOperationConfig
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GitResult:

   .. graphviz::
      :align: center

      digraph inheritance_GitResult {
        node [shape=record];
        "GitResult" [label="GitResult"];
        "pydantic.BaseModel" -> "GitResult";
      }

.. autopydantic_model:: tools.tools.toolkits.dev.tools.GitResult
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QualityResult:

   .. graphviz::
      :align: center

      digraph inheritance_QualityResult {
        node [shape=record];
        "QualityResult" [label="QualityResult"];
        "pydantic.BaseModel" -> "QualityResult";
      }

.. autopydantic_model:: tools.tools.toolkits.dev.tools.QualityResult
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RenameClassTransformer:

   .. graphviz::
      :align: center

      digraph inheritance_RenameClassTransformer {
        node [shape=record];
        "RenameClassTransformer" [label="RenameClassTransformer"];
        "BaseTransformer" -> "RenameClassTransformer";
      }

.. autoclass:: tools.tools.toolkits.dev.tools.RenameClassTransformer
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RenameFunctionTransformer:

   .. graphviz::
      :align: center

      digraph inheritance_RenameFunctionTransformer {
        node [shape=record];
        "RenameFunctionTransformer" [label="RenameFunctionTransformer"];
        "BaseTransformer" -> "RenameFunctionTransformer";
      }

.. autoclass:: tools.tools.toolkits.dev.tools.RenameFunctionTransformer
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TransformerContext:

   .. graphviz::
      :align: center

      digraph inheritance_TransformerContext {
        node [shape=record];
        "TransformerContext" [label="TransformerContext"];
      }

.. autoclass:: tools.tools.toolkits.dev.tools.TransformerContext
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.dev.tools
   :collapse:
   
.. autolink-skip:: next
