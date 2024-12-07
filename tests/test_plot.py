from mylib import *
import pytest

@pytest.mark.parametrize('save',[True,False])
def test_hooks(save):
    plot_kw = dict(figsize=(30,8),show=False,save=save,title='test-hooks' if save else None)
    plot_hook(
        lambda : plt.plot([1,2,3,4]),
        **plot_kw
    )


