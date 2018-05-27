import allure, pytest
class Test_allure:
    def setup(self):
         print("1231")
    def teardown(self):
         pass
    @pytest.mark.parametrize("a",[1,2,3])
    @allure.step('我是测试步骤001')
    def test_al(self, a):
        assert a != 2

    @allure.step('我是测试步骤002')
    @pytest.mark.parametrize("a", [1, 5, 6])
    def test_a2(self, a):
        assert a != 2