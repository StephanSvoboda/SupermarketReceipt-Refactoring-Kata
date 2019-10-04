import pytest

from model_objects import Product, SpecialOfferType, ProductUnit
from shopping_cart import ShoppingCart
from teller import Teller
from tests.fake_catalog import FakeCatalog

@pytest.fixture
def catalog() :
    return FakeCatalog()

def _test_API_DEMO_MICHAEL():
    catalog = FakeCatalog()
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    catalog.add_product(toothbrush, 0.99)

    apples = Product("apples", ProductUnit.KILO)
    catalog.add_product(apples, 1.99)

    teller = Teller(catalog)
    teller.add_special_offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, toothbrush, 10.0)

    cart = ShoppingCart()
    cart.add_item_quantity(apples, 2.5)

    receipt = teller.checks_out_articles_from(cart)

    assert 4.975 == pytest.approx(receipt.total_price(), 0.01)
    assert [] == receipt.discounts
    assert 1 == len(receipt.items)
    receipt_item = receipt.items[0]
    assert apples == receipt_item.product
    assert 1.99 == receipt_item.price
    assert 2.5 * 1.99 == pytest.approx(receipt_item.total_price, 0.01)
    assert 2.5 == receipt_item.quantity


def _test_toothbrush_two_for_one():
    catalog = FakeCatalog()
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    catalog.add_product(toothbrush, 0.99)
    teller = Teller(catalog)
    teller.add_special_offer(SpecialOfferType.TWO_FOR_AMOUNT, toothbrush, 1)
    cart = ShoppingCart()
    cart.add_item_quantity(toothbrush, 2)
    receipt = teller.checks_out_articles_from(cart)

    assert 0.99 == pytest.approx(receipt.total_price(), 0.01)
    assert 1 == len(receipt.items)
    receipt_item = receipt.items[0]
    assert 0.99 == receipt_item.price
    assert 2 == receipt_item.quantity

def test_touthbrush_single(catalog):
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    catalog.add_product(toothbrush, 0.99)

    teller = Teller(catalog)
    teller.add_special_offer(SpecialOfferType.THREE_FOR_TWO, toothbrush, 1)
    cart = ShoppingCart()
    cart.add_item_quantity(toothbrush, 1)
    receipt = teller.checks_out_articles_from(cart)

    assert 0.99 == pytest.approx(receipt.total_price(), 0.01)
    assert 1 == len(receipt.items)
    receipt_item = receipt.items[0]
    assert 0.99 == receipt_item.price
    assert 1 == receipt_item.quantity

def test_touthbrush_double(catalog):
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    catalog.add_product(toothbrush, 0.99)
    teller = Teller(catalog)
    cart = ShoppingCart()
    cart.add_item_quantity(toothbrush, 2)
    receipt = teller.checks_out_articles_from(cart)

    assert 1.98 == pytest.approx(receipt.total_price(), 0.01)
    assert 1 == len(receipt.items)
    receipt_item = receipt.items[0]
    assert 0.99 == receipt_item.price
    assert 2 == receipt_item.quantity

def test_touthbrush_double_discount(catalog):
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    catalog.add_product(toothbrush, 0.99)
    teller = Teller(catalog)
    teller.add_special_offer(SpecialOfferType.THREE_FOR_TWO, toothbrush, 0.99)
    cart = ShoppingCart()
    cart.add_item_quantity(toothbrush, 2)
    receipt = teller.checks_out_articles_from(cart)

    assert 1.98 == pytest.approx(receipt.total_price(), 0.01)
    assert 1 == len(receipt.items)
    receipt_item = receipt.items[0]
    assert 0.99 == receipt_item.price
    assert 2 == receipt_item.quantity


def test_touthbrush_triple_discount(catalog):
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    catalog.add_product(toothbrush, 0.99)
    teller = Teller(catalog)
    teller.add_special_offer(SpecialOfferType.THREE_FOR_TWO, toothbrush, 0.99)
    cart = ShoppingCart()
    cart.add_item_quantity(toothbrush, 3)
    receipt = teller.checks_out_articles_from(cart)

    assert 1.98 == receipt.total_price()
    assert 1 == len(receipt.items)
    receipt_item = receipt.items[0]
    assert 0.99 == receipt_item.price
    assert 3 == receipt_item.quantity

def test_touthbrush_quad_discount(catalog):
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    catalog.add_product(toothbrush, 0.99)
    teller = Teller(catalog)
    teller.add_special_offer(SpecialOfferType.THREE_FOR_TWO, toothbrush, 0.99)
    cart = ShoppingCart()
    cart.add_item_quantity(toothbrush, 4)
    receipt = teller.checks_out_articles_from(cart)

    assert 2.97 == pytest.approx(receipt.total_price(),0.01)
    assert 1 == len(receipt.items)
    receipt_item = receipt.items[0]
    assert 0.99 == receipt_item.price
    assert 4 == receipt_item.quantity

def test_touthbrush_five_discount(catalog):
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    catalog.add_product(toothbrush, 0.99)
    teller = Teller(catalog)
    teller.add_special_offer(SpecialOfferType.THREE_FOR_TWO, toothbrush, 0.99)
    cart = ShoppingCart()
    cart.add_item_quantity(toothbrush, 5)
    receipt = teller.checks_out_articles_from(cart)

    assert 3.96 == pytest.approx(receipt.total_price(),0.01)
    assert 1 == len(receipt.items)
    receipt_item = receipt.items[0]
    assert 0.99 == receipt_item.price
    assert 5 == receipt_item.quantity

def test_touthbrush_six_discount(catalog):
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    catalog.add_product(toothbrush, 0.99)
    teller = Teller(catalog)
    teller.add_special_offer(SpecialOfferType.THREE_FOR_TWO, toothbrush, 0.99)
    cart = ShoppingCart()
    cart.add_item_quantity(toothbrush, 6)
    receipt = teller.checks_out_articles_from(cart)

    assert 3.96 == pytest.approx(receipt.total_price(),0.01)
    assert 1 == len(receipt.items)
    receipt_item = receipt.items[0]
    assert 0.99 == receipt_item.price
    assert 6 == receipt_item.quantity 

@pytest.mark.parametrize("total_price, quantity",
[(1.99, 1), (3.98, 2), (2.985, 1.5)])
def test_kilo_nodiscount(catalog, total_price, quantity):
    apple = Product("apple", ProductUnit.KILO)
    catalog.add_product(apple, 1.99)
    teller = Teller(catalog)
    cart = ShoppingCart()
    cart.add_item_quantity(apple, quantity)
    receipt = teller.checks_out_articles_from(cart)

    assert total_price == receipt.total_price()
    assert 1 == len(receipt.items)
    receipt_item = receipt.items[0]
    assert 1.99 == receipt_item.price
    assert quantity == receipt_item.quantity

@pytest.mark.parametrize("total_price, quantity",
[(1.99*0.8, 1), (3.98*0.8, 2), (2.985*0.8, 1.5)])
def test_kilo_discount(catalog, total_price, quantity):
    apple = Product("apple", ProductUnit.KILO)
    catalog.add_product(apple, 1.99)
    teller = Teller(catalog)
    teller.add_special_offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, apple, 20.0)

    cart = ShoppingCart()
    cart.add_item_quantity(apple, quantity)
    receipt = teller.checks_out_articles_from(cart)

    assert total_price == receipt.total_price()
    assert 1 == len(receipt.items)
    receipt_item = receipt.items[0]
    assert 1.99 == receipt_item.price
    assert quantity == receipt_item.quantity

@pytest.mark.parametrize("total_price, quantity",
[(2.49*0.9, 1), (4.98*0.9, 2), (2.49*1.5*0.9, 1.5)])
def test_each_percent_discount(catalog, total_price, quantity):
    product = Product("rice", ProductUnit.EACH)
    catalog.add_product(product, 2.49)
    teller = Teller(catalog)
    teller.add_special_offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, product, 10.0)
    cart = ShoppingCart()
    cart.add_item_quantity(product, quantity)
    receipt = teller.checks_out_articles_from(cart)

    assert total_price == receipt.total_price()
    assert 1 == len(receipt.items)
    receipt_item = receipt.items[0]
    assert 2.49 == receipt_item.price
    assert quantity == receipt_item.quantity

@pytest.mark.parametrize("total_price, quantity",
[(1.79*4, 4), (7.49, 5),(7.49+1.79,6)])
def test_five_for_special_price(catalog,total_price,quantity):
    product = Product("toothpaste",ProductUnit.EACH)
    catalog.add_product(product,1.79)
    teller = Teller(catalog)
    teller.add_special_offer(SpecialOfferType.FIVE_FOR_AMOUNT,product,7.49)
    cart = ShoppingCart()
    cart.add_item_quantity(product,quantity)
    receipt = teller.checks_out_articles_from(cart)

    assert total_price == receipt.total_price()
    assert 1 == len(receipt.items)
    receipt_item = receipt.items[0]
    assert 1.79 == receipt_item.price
    assert quantity == receipt_item.quantity