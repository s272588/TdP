import flet as ft
from Classroom.GestoreCorsi.model.model import Model
from Classroom.GestoreCorsi.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._pd = None


    def get_corsi_periodo(self, e):
        if self._pd is None:
            self._view.create_alert("Selezionare un periodo didattico")
            return

        else:
            corsi = self._model.get_corsi_periodo(self._pd)
            self._view.lst_result.controls.clear()
            for corso in corsi:
                self._view.lst_result.controls.append(ft.Text(corso))

            self._view.update_page()


    def get_studenti_periodo(self, e):
        if self._pd is None:
            self._view.create_alert("Selezionare un periodo didattico")
            return

        numero_studenti = self._model.get_studenti_periodo(self._pd)
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text(f'Gli studenti iscritti ai corsi del primo periodo didattico {self._pd} sono {numero_studenti}'))
        self._view.update_page()

    def get_studenti_corso(self,e):
        self._view.lst_result.controls.clear()
        codiceCorso = self._view.txt_codice_corso.value
        studenti_corso = self._model.get_studenti_corso(codiceCorso)
        self._view.lst_result.controls.append(ft.Text(f'Il corso ha {len(studenti_corso)} iscritti:'))
        for studente in studenti_corso:
            self._view.lst_result.controls.append(ft.Text(studente.__str__()))
        self._view.update_page()


    def get_dettaglio_corso(self,e):
        self._view.lst_result.controls.clear()
        codiceCorso = self._view.txt_codice_corso.value
        dettagli_corso = self._model.getDettagliCorso(codiceCorso)
        self._view.lst_result.controls.append(ft.Text(f'Gli studenti nel corso {codiceCorso} sono divisi in questa maniera:'))
        for cds, studenti in dettagli_corso.items():
            self._view.lst_result.controls.append(ft.Text(f'{cds}: {studenti} studenti'))

        self._view.update_page()
    def leggi_tendina(self, e):
        self._pd = self._view.dd_periodo.value
        print(self._pd)

