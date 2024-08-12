from abc import ABC, abstractmethod


class ViewEngine(ABC):
    @abstractmethod
    def render(self, view_name, data):
        pass


class MatchaViewEngine(ViewEngine):
    def render(self, view_name, data):
        return "View rendered by 'Matcha'"


class Controller:
    def render(self, view_name, data):
        engine = self._create_view_engine()
        html = engine.render(view_name, data)
        print(html)

    # Create this method either as an abstract method or default implementation
    def _create_view_engine(self) -> ViewEngine:
        return MatchaViewEngine()


class SharpViewEngine(ViewEngine):
    def render(self, view_name, data):
        return "View rendered by 'Sharp'"


class SharpController(Controller):
    def _create_view_engine(self) -> ViewEngine:
        return SharpViewEngine()


class ProductsController(SharpController):
    def list_products(self):
        # Get products from a database
        data = {}
        # data['name'] = value
        self.render('products.html', data)


if __name__ == '__main__':
    controller = ProductsController()
    controller.list_products()
