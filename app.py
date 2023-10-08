from time import monotonic

from textual import on
from textual.app import App
from textual.reactive import reactive
from textual.containers import ScrollableContainer
from textual.widgets import Button, Footer, Header, Static

class TimeDisplay(Static):
    time_elapsed = reactive(0)
    start_time = monotonic()

    def watch_time_elapsed(self):
        time = self.time_elapsed
        self.update(str(time))

    def start(self):
        self.start_time = monotonic()
        self.time_elapsed = 0
        pass

    def stop(self):
        self.time_elapsed = monotonic() - self.start_time
        pass

    def reset(self):
        self.time_elapsed = 0
        pass

class Stopwatch(Static):
    @on(Button.Pressed, '#start')
    def start_stopwatch(self):
        self.add_class("started")
        self.query_one(TimeDisplay).start()
        
    @on(Button.Pressed, '#stop')
    def stop_stopwatch(self):
        self.remove_class("started")
        self.query_one(TimeDisplay).stop()

    @on(Button.Pressed, '#reset')
    def reset_stopwatch(self):
        self.remove_class("started")
        self.query_one(TimeDisplay).reset()
    
    def compose(self):
        yield Button('Start', variant="success", id="start")
        yield Button('Stop', variant="error", id="stop", classes="hidden")
        yield Button('Reset', id="reset")
        yield TimeDisplay('00:00:00.00', id="time")

class ModelPrompter(App):
    BINDINGS = [
        ('d', 'toggle_dark_mode', 'Toggle dark mode')
    ]

    CSS_PATH = "app.css"

    def compose(self):
        yield Header(show_clock=True)
        with ScrollableContainer(id="stopwatches"):
            yield Stopwatch(classes="started")
            yield Stopwatch()
            yield Stopwatch()
        yield Footer()

    def action_toggle_dark_mode(self):
        self.dark = not self.dark

if __name__ == "__main__":
    ModelPrompter().run()