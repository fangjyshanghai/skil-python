import pytest
import skil


work_space = None  # because number of workspaces is limited
_sk = None


def _get_sk():
    global _sk
    if _sk is None:
        _sk = skil.Skil()
    return _sk


def _get_ws():
    global work_space
    if work_space is not None:
        return work_space
    sk = _get_sk()
    work_space = skil.WorkSpace(sk)
    return work_space


def test_work_space_by_id():
    global work_space
    global work_space_id
    sk = _get_sk()
    work_space = skil.WorkSpace(sk, name='test_ws')
    id = work_space.id
    work_space_id = id
    work_space2 = skil.get_workspace_by_id(sk, id)
    assert work_space.name == work_space2.name


def test_experiment_by_id():
    ws = _get_ws()
    exp = skil.Experiment(ws, name='test_exp')
    id = exp.id
    exp2 = skil.get_experiment_by_id(ws, id)
    assert exp.name == exp2.name


def test_deployment_by_id():
    sk = _get_sk()
    dep = skil.Deployment(sk, name='test_dep')
    id = dep.id
    dep2 = skil.get_deployement_by_id(sk, id)
    assert dep.name == dep2.name


def test_model_by_id():
    ws = _get_ws()
    exp = skil.Experiment(ws, name='test_exp2')
    model = skil.Model('model.h5', name='test_model', experiment=exp)
    id = model.id
    model2 = skil.get_model_by_id(exp, id)
    assert model.name == model2.name

if __name__ == '__main__':
    pytest.main([__file__])