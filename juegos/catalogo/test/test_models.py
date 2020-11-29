from django.test import TestCase
from catalogo.models import Game

class GameTestCase(TestCase):

    def setUp(self):
        Game.objects.create(nombre="Mario Bros", creador="Shigeru Miyamoto", descripcion="blablabla")


    

    def test_juegos(self):
        juego = Game.objects.get(nombre="Mario Bros")
        self.assertEqual(juego.nombre, "Mario Bros")