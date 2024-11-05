"""
Questo modulo fornisce la classe NextStep per la creazione di elementi call-to-action
in visualizzazioni Story. È progettato per lavorare in congiunzione con la classe Story
per creare visualizzazioni di dati narrative.
"""

class NextStep:
    """
    Classe per la creazione di elementi call-to-action in visualizzazioni Story.
    Supporta tre tipi di visualizzazione: button, line_steps e stair_steps.
    
    Questa classe può essere utilizzata sia direttamente che attraverso i parametri
    nominali nella classe Story:

    Examples:
        >>> # Usando il parametro button
        >>> story.add_call_to_action(
        ...     button=NextStep(
        ...         type='button',
        ...         text='Click me',
        ...         url='https://example.com'
        ...     )
        ... )
        
        >>> # Usando il parametro stairs
        >>> story.add_call_to_action(
        ...     stairs=NextStep(
        ...         type='stair_steps',
        ...         texts=['Base', 'Intermedio', 'Avanzato']
        ...     )
        ... )
        
        >>> # Usando il parametro line
        >>> story.add_call_to_action(
        ...     line=NextStep(
        ...         type='line_steps',
        ...         texts=['Step 1', 'Step 2', 'Step 3']
        ...     )
        ... )
    """
    
    def __init__(
        self,
        type: str,
        position: str = 'bottom',
        # Parametri per testo e contenuto
        title: str = "What can we do next?",
        texts: list = None,
        text: str = None,
        url: str = None,
        # Parametri per i colori
        primary_color: str = '#80C11E',
        text_color: str = 'black',
        title_color: str = 'black',
        opacity: float = 0.2,
        # Parametri per i font
        font_family: str = 'Arial',
        font_size: int = 14,
        title_font_size: int = None,
        title_font_family: str = None,
        # Parametri dimensionali per button
        button_width: int = 120,
        button_height: int = 40,
        button_corner_radius: int = 5,
        # Parametri dimensionali per line_steps
        rect_width: int = 10,
        rect_height: int = 10,
        rect_space: int = 5,
        chart_width: int = 700,
        chart_height: int = 100,
        # Parametri dimensionali specifici per stair_steps
        stair_height: int = 3
    ):
        """
        Inizializza una configurazione NextStep.
        
        Args:
            type (str): Tipo di visualizzazione ('button', 'line_steps', 'stair_steps')
            position (str, optional): Posizione dell'elemento. Default 'bottom'
            title (str, optional): Titolo della visualizzazione. Default "What can we do next?"
            texts (list, optional): Lista di testi per gli steps. Default None
            text (str, optional): Testo per il bottone. Default None
            url (str, optional): URL per il bottone. Default None
            primary_color (str, optional): Colore principale. Default '#80C11E'
            text_color (str, optional): Colore del testo. Default 'black'
            title_color (str, optional): Colore del titolo. Default 'black'
            opacity (float, optional): Opacità degli elementi. Default 0.2
            font_family (str, optional): Font principale. Default 'Arial'
            font_size (int, optional): Dimensione font principale. Default 14
            title_font_size (int, optional): Dimensione font titolo. Default None
            title_font_family (str, optional): Font del titolo. Default None
            button_width (int, optional): Larghezza bottone. Default 120
            button_height (int, optional): Altezza bottone. Default 40
            button_corner_radius (int, optional): Raggio angoli bottone. Default 5
            rect_width (int, optional): Larghezza rettangoli steps. Default 10
            rect_height (int, optional): Altezza rettangoli line_steps. Default 10
            rect_space (int, optional): Spazio tra rettangoli steps. Default 5
            chart_width (int, optional): Larghezza totale grafico. Default 700
            chart_height (int, optional): Altezza totale grafico. Default 100
            stair_height (int, optional): Altezza gradini stair_steps. Default 3
        
        Raises:
            ValueError: Se il tipo non è valido o se mancano parametri obbligatori
        """
        # Verifica che il tipo sia valido
        valid_types = ['line_steps', 'button', 'stair_steps']
        if type not in valid_types:
            raise ValueError(f"Type deve essere uno tra: {', '.join(valid_types)}")
        
        # Memorizza i parametri base
        self.type = type
        self.position = position
        
        # Gestione del contenuto
        # Il titolo è None per i button dato che non lo utilizzano
        self.title = None if type == 'button' else title
        self.texts = texts or []  # Lista vuota se None
        self.text = text
        self.url = url
        
        # Memorizza i parametri di stile
        self.primary_color = primary_color
        self.text_color = text_color
        self.title_color = title_color
        self.opacity = opacity
        
        # Gestione dei font
        self.font_family = font_family
        self.font_size = font_size
        # Se title_font_size non è specificato, usa un multiplo del font_size base
        self.title_font_size = title_font_size or (font_size * 1.4)
        # Se title_font_family non è specificato, usa il font_family base
        self.title_font_family = title_font_family or font_family
        
        # Configurazione delle dimensioni per ogni tipo di visualizzazione
        self.dimensions = {
            # Dimensioni specifiche per i bottoni
            'button': {
                'width': button_width,
                'height': button_height,
                'corner_radius': button_corner_radius
            },
            # Dimensioni per i line_steps
            'line_steps': {
                'rect_width': rect_width,
                'rect_height': rect_height,
                'space': rect_space,
                'chart_width': chart_width,
                'chart_height': chart_height
            },
            # Dimensioni per gli stair_steps
            'stair_steps': {
                'rect_width': rect_width,
                'rect_height': stair_height,  # usa stair_height invece di rect_height
                'chart_width': chart_width,
                'chart_height': chart_height
            }
        }
        
        # Esegue la validazione della configurazione
        self._validate_configuration()
    
    def _validate_configuration(self):
        """
        Valida la configurazione in base al tipo selezionato.
        
        Raises:
            ValueError: Se la configurazione non è valida per il tipo selezionato
        """
        if self.type == 'button':
            # Per i bottoni serve sia il testo che l'URL
            if not self.text:
                raise ValueError("Il parametro 'text' è richiesto per il tipo button")
            if not self.url:
                raise ValueError("Il parametro 'url' è richiesto per il tipo button")
        
        elif self.type in ['line_steps', 'stair_steps']:
            # Per gli steps serve una lista di testi valida
            if not self.texts:
                raise ValueError(f"È necessaria una lista di testi per {self.type}")
            if not isinstance(self.texts, list):
                raise ValueError(f"Il parametro 'texts' deve essere una lista per {self.type}")
            if len(self.texts) > 5:
                raise ValueError("Il numero massimo di steps è 5")
            if len(self.texts) < 1:
                raise ValueError("Deve essere fornito almeno uno step")

    def to_dict(self):
        """
        Converte la configurazione in un dizionario compatibile con Story.add_call_to_action.
        
        Returns:
            dict: Dizionario contenente tutti i parametri necessari per la configurazione
        """
        # Configurazione di base comune a tutti i tipi
        config = {
            'type': self.type,
            'position': self.position,
            'title': self.title,
            'font_family': self.font_family,
            'font_size': self.font_size,
            'title_font_size': self.title_font_size,
            'title_font_family': self.title_font_family,
            'title_color': self.title_color
        }
        
        # Aggiunge configurazione specifica in base al tipo
        if self.type == 'button':
            config.update({
                'text': self.text,
                'url': self.url,
                'button_color': self.primary_color,
                'button_text_color': self.text_color,
                'button_opacity': self.opacity,
                'button_width': self.dimensions['button']['width'],
                'button_height': self.dimensions['button']['height'],
                'button_corner_radius': self.dimensions['button']['corner_radius']
            })
        
        elif self.type == 'line_steps':
            config.update({
                'texts': self.texts,
                'line_steps_color': self.primary_color,
                'line_steps_text_color': self.text_color,
                'line_steps_opacity': self.opacity,
                'line_steps_rect_width': self.dimensions['line_steps']['rect_width'],
                'line_steps_rect_height': self.dimensions['line_steps']['rect_height'],
                'line_steps_space': self.dimensions['line_steps']['space'],
                'line_steps_chart_width': self.dimensions['line_steps']['chart_width'],
                'line_steps_chart_height': self.dimensions['line_steps']['chart_height']
            })
        
        elif self.type == 'stair_steps':
            config.update({
                'texts': self.texts,
                'stair_steps_color': self.primary_color,
                'stair_steps_text_color': self.text_color,
                'stair_steps_opacity': self.opacity,
                'stair_steps_rect_width': self.dimensions['stair_steps']['rect_width'],
                'stair_steps_rect_height': self.dimensions['stair_steps']['rect_height'],
                'stair_steps_chart_width': self.dimensions['stair_steps']['chart_width'],
                'stair_steps_chart_height': self.dimensions['stair_steps']['chart_height']
            })
        
        return config
    
    def __repr__(self):
        """
        Fornisce una rappresentazione stringa dell'oggetto NextStep.
        
        Returns:
            str: Rappresentazione stringa dell'oggetto
        """
        return f"NextStep(type='{self.type}', position='{self.position}')"
