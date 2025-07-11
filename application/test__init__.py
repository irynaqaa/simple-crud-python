import pytest
from application import app


def test_app_import():
    assert app is not None


def test_app_run():
    assert app.run(debug=True) is None


def test_app_debug_modes():
    assert app.run(debug=True) is None
    assert app.run(debug=False) is None


def test_app_error_handling():
    with pytest.raises(ImportError):
        from application import non_existent_module
    with pytest.raises(AttributeError):
        app.non_existent_attribute
    with pytest.raises(RuntimeError):
        app.run(debug=True)


def test_app_edge_cases():
    assert app.run(debug=True) is None
    assert app.run(debug=False) is None
