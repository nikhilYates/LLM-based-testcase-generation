# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import call_trees as module_0
import tensorflow.python.autograph.pyct.anno as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    arg_template_builder_0 = module_0._ArgTemplateBuilder()
    var_0 = arg_template_builder_0.finalize()
    module_1.dup(arg_template_builder_0, arg_template_builder_0)


def test_case_1():
    arg_template_builder_0 = module_0._ArgTemplateBuilder()
    with pytest.raises(AssertionError):
        arg_template_builder_0.to_ast()


def test_case_2():
    function_0 = module_0._Function()


def test_case_3():
    arg_template_builder_0 = module_0._ArgTemplateBuilder()
    arg_template_builder_1 = module_0._ArgTemplateBuilder()
    var_0 = arg_template_builder_1.add_arg(arg_template_builder_0)


def test_case_4():
    arg_template_builder_0 = module_0._ArgTemplateBuilder()
    arg_template_builder_1 = module_0._ArgTemplateBuilder()
    none_type_0 = None
    var_0 = arg_template_builder_0.add_stararg(none_type_0)
    with pytest.raises(AssertionError):
        arg_template_builder_0.to_ast()


@pytest.mark.xfail(strict=True)
def test_case_5():
    none_type_0 = None
    module_0.transform(none_type_0, none_type_0)