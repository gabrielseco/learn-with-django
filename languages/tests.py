from django.test import TestCase
from languages.models import Language
# Create your tests here.

class LanguageModelTest(TestCase):

    def test_the_language_model(self):
       """
        The model must have
        name Text
        code Text
        url  Text that point for an asset

       :return:
       """
       model = Language()
       model.name = 'Spanish'

       model.code = 'es'

       model.url = '/static/img/languages/spanish.png';

       model.save()

       saved_items = Language.objects.all()

       self.assertEqual(saved_items.count(), 1)


    def test_unicode(self):
        """
        It should test the unicode name of the object
        :return:
        """

        model = Language.objects.filter(pk=1)

        self.assertTrue(model.__str__(), 'Spanish')



