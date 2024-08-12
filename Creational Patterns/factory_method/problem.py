from abc import ABC, abstractmethod


class ViewEngine(ABC):
    @abstractmethod
    def render(self, view_name, data):
        pass


class MatchaViewEngine(ViewEngine):
    def render(self, view_name, data):
        return "View rendered by 'Matcha'"


class Controller:
    def render(self, view_name, data, engine: ViewEngine):
        # engine = MatchaViewEngine()
        html = engine.render(view_name, data)
        print(html)


class ProductsController(Controller):
    def list_products(self):
        # Get products from a database
        data = {}
        # data['name'] = value
        self.render('products.html', data, MatchaViewEngine())


if __name__ == '__main__':
    controller = ProductsController()
    controller.list_products()
