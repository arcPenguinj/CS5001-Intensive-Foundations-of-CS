from fence import Fence

def test_Constructor():
    fence = Fence("picket", 12.2)
    assert(fence.style == "picket")
    assert(fence.price_per_foot == 12.2)

def test_get_cost():
    fence = Fence("picket", 4)
    assert(fence.get_cost(3) == 24)
    assert(fence.get_cost(6) == 24)
    assert(fence.get_cost(10) == 40)
    assert(fence.get_cost(100) == 400)
    assert(fence.get_cost(101) == 384)
