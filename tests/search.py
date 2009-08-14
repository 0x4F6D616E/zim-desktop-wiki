
from tests import get_test_notebook, TestCase

from zim.search import *
from zim.notebook import Path


class TestSearch(TestCase):

	def runTest(self):
		query = Query('foo bar')
		self.assertEqual(query.root,
			AndGroup([('content', 'foo'), ('content', 'bar')]) )

		notebook = get_test_notebook()
		searcher = Searcher(notebook)
		result = searcher.search(query)
		self.assertTrue(isinstance(result, ResultsSelection))
		self.assertTrue(len(result.pages) > 0)
		self.assertTrue(Path('TODOList:bar') in result.pages)
		scores = [result.scores[p] for p in result.pages]
		self.assertTrue(all(scores))

		#~ print result.pages

		notebook.index.update()
		query = Query('LinksTo: "Test:Foo:Bar"')
		self.assertEqual(query.root,
			AndGroup([('linksto', 'Test:Foo:Bar')]) )
		result = searcher.search(query)
		self.assertTrue(isinstance(result, ResultsSelection))
		self.assertTrue(Path('TODOList:bar') in result.pages)
		scores = [result.scores[p] for p in result.pages]
		self.assertTrue(all(scores))

		#~ print result.pages

# TODO subclass with file based notebook to test the 'grep' optimalisation
