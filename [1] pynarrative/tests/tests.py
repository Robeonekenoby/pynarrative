import unittest
import pandas as pd
import altair as alt
from pynarrative import Story
from pynarrative import NextStep

class TestStoryInitialization(unittest.TestCase):
    def setUp(self):
        print(f"\nExecuting: {self._testMethodName}")
        
    def test_basic_initialization(self):
        """Test inizializzazione base di Story."""
        data = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
        story = Story(data, width=600, height=400)
        self.assertIsInstance(story.chart, alt.Chart)
        self.assertEqual(story.chart.width, 600)
        self.assertEqual(story.chart.height, 400)
        print("✓ Base initialization successful")

    def test_initialization_without_data(self):
        """Test inizializzazione Story senza dati."""
        story = Story(width=500, height=300)
        self.assertIsInstance(story.chart, alt.Chart)
        self.assertIsNone(story.chart.data)
        print("✓ No-data initialization successful")

    def test_custom_font_and_size(self):
        """Test inizializzazione con font e dimensione personalizzati."""
        story = Story(font='Helvetica', base_font_size=18)
        self.assertEqual(story.font, 'Helvetica')
        self.assertEqual(story.base_font_size, 18)
        print("✓ Custom font initialization successful")

    def test_default_values(self):
        """Test valori predefiniti dell'inizializzazione."""
        story = Story()
        self.assertEqual(story.font, 'Arial')
        self.assertEqual(story.base_font_size, 16)
        print("✓ Default values correct")

class TestStoryElements(unittest.TestCase):
    def setUp(self):
        print(f"\nExecuting: {self._testMethodName}")
        self.data = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
        self.story = Story(self.data)

    def test_add_title(self):
        """Test aggiunta titolo."""
        self.story.add_title("Main Title", subtitle="Subtitle")
        last_layer = self.story.story_layers[-1]
        self.assertEqual(last_layer['type'], 'title')
        self.assertEqual(last_layer['title'], "Main Title")
        print("✓ Title added successfully")

    def test_add_context(self):
        """Test aggiunta contesto."""
        self.story.add_context("Context text", position="top")
        last_layer = self.story.story_layers[-1]
        self.assertEqual(last_layer['type'], 'context')
        self.assertEqual(last_layer['text'], "Context text")
        print("✓ Context added successfully")

class TestCallToAction(unittest.TestCase):
    def setUp(self):
        print(f"\nExecuting: {self._testMethodName}")
        self.story = Story()

    def test_basic_call_to_action(self):
        """Test call-to-action base."""
        self.story.add_call_to_action("Click here")
        last_layer = self.story.story_layers[-1]
        self.assertEqual(last_layer['type'], 'cta')
        print("✓ Basic CTA added successfully")

    def test_line_steps_call_to_action(self):
        """Test call-to-action con line steps."""
        texts = ["Step 1", "Step 2", "Step 3"]
        self.story.add_call_to_action(type='line_steps', texts=texts)
        last_layer = self.story.story_layers[-1]
        self.assertEqual(last_layer['type'], 'special_cta')
        self.assertTrue(isinstance(last_layer['chart'], (alt.Chart, alt.LayerChart)))
        print("✓ Line steps CTA added successfully")

    def test_stair_steps_call_to_action(self):
        """Test call-to-action con stair steps."""
        texts = ["Step 1", "Step 2"]
        self.story.add_call_to_action(type='stair_steps', texts=texts)
        last_layer = self.story.story_layers[-1]
        self.assertEqual(last_layer['type'], 'special_cta')
        self.assertTrue(isinstance(last_layer['chart'], (alt.Chart, alt.LayerChart)))
        print("✓ Stair steps CTA added successfully")

    def test_nextstep_button(self):
        """Test call-to-action con NextStep button."""
        button = NextStep(
            type='button',
            text='Click me',
            url='https://example.com'
        )
        self.story.add_call_to_action(button=button)
        last_layer = self.story.story_layers[-1]
        self.assertEqual(last_layer['type'], 'special_cta')
        print("✓ NextStep button added successfully")

    def test_nextstep_line_steps(self):
        """Test call-to-action con NextStep line steps."""
        line = NextStep(
            type='line_steps',
            texts=['Step 1', 'Step 2', 'Step 3']
        )
        self.story.add_call_to_action(line=line)
        last_layer = self.story.story_layers[-1]
        self.assertEqual(last_layer['type'], 'special_cta')
        print("✓ NextStep line steps added successfully")

    def test_nextstep_stair_steps(self):
        """Test call-to-action con NextStep stair steps."""
        stairs = NextStep(
            type='stair_steps',
            texts=['Base', 'Intermediate', 'Advanced']
        )
        self.story.add_call_to_action(stairs=stairs)
        last_layer = self.story.story_layers[-1]
        self.assertEqual(last_layer['type'], 'special_cta')
        print("✓ NextStep stair steps added successfully")

class TestAnnotations(unittest.TestCase):
    def setUp(self):
        print(f"\nExecuting: {self._testMethodName}")
        self.data = pd.DataFrame({'x': range(1, 6), 'y': [10, 20, 15, 25, 30]})
        self.story = Story(self.data)
        self.story.encode(x='x:Q', y='y:Q')

    def test_basic_annotation(self):
        """Test annotazione base."""
        self.story.add_annotation(x_point=3, y_point=15, annotation_text="Peak")
        last_layer = self.story.story_layers[-1]
        self.assertEqual(last_layer['type'], 'annotation')
        print("✓ Basic annotation added successfully")

    def test_arrow_directions(self):
        """Test direzioni frecce nelle annotazioni."""
        directions = ['left', 'right', 'up', 'down', 'upleft', 'upright', 
                     'downleft', 'downright', 'leftup', 'leftdown', 
                     'rightup', 'rightdown', 'upleftcurve', 'uprightcurve']
        for direction in directions:
            self.story.add_annotation(
                x_point=3,
                y_point=15,
                annotation_text=f"Direction {direction}",
                arrow_direction=direction
            )
            print(f"✓ Arrow direction '{direction}' works")

    def test_annotation_customization(self):
        """Test personalizzazione delle annotazioni."""
        self.story.add_annotation(
            x_point=3,
            y_point=15,
            annotation_text="Custom annotation",
            arrow_color='red',
            arrow_size=50,
            label_color='blue',
            label_size=14,
            show_point=True,
            point_color='green',
            point_size=80
        )
        print("✓ Annotation customization works")

class TestErrorHandling(unittest.TestCase):
    def setUp(self):
        print(f"\nExecuting: {self._testMethodName}")
        self.story = Story()

    def test_invalid_inputs(self):
        """Test gestione input non validi."""
        with self.assertRaises(ValueError):
            self.story.add_annotation(1, 1, arrow_direction='invalid')
        print("✓ Invalid arrow direction caught")

        with self.assertRaises(ValueError):
            self.story.add_call_to_action(type='line_steps', texts=[])
        print("✓ Empty line steps caught")

        with self.assertRaises(ValueError):
            self.story.add_call_to_action(type='stair_steps', texts="not a list")
        print("✓ Invalid stair steps input caught")

        with self.assertRaises(ValueError):
            invalid_nextstep = NextStep(type='invalid_type', texts=['Step 1'])
        print("✓ Invalid NextStep type caught")

class TestConfiguration(unittest.TestCase):
    def setUp(self):
        print(f"\nExecuting: {self._testMethodName}")
        self.story = Story()

    def test_configure_view(self):
        """Test configurazione della vista."""
        self.story.configure_view(strokeWidth=0, fill='#f0f0f0')
        self.assertIn('view', self.story.config)
        self.assertEqual(self.story.config['view']['strokeWidth'], 0)
        self.assertEqual(self.story.config['view']['fill'], '#f0f0f0')
        print("✓ View configuration works")

if __name__ == '__main__':
    print("\n=== Starting Story Tests ===")
    unittest.main(verbosity=2)
