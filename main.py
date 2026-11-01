from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import MDList, TwoLineAvatarIconListItem
from kivymd.uix.button import MDRaisedButton
import sqlite3, json, re

DB = "buio_chef.db"

def init_db():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ricette (id INTEGER PRIMARY KEY, titolo TEXT, categoria TEXT, video_path TEXT, fonte TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS ingredienti (id INTEGER PRIMARY KEY, ricetta_id INTEGER, nome TEXT, quantita TEXT, spuntato INTEGER DEFAULT 0)")
    con.commit(); con.close()

class BuioChefApp(MDApp):
    def build(self):
        init_db()
        self.title="Buio Chef SMART COUPLE"
        lay=BoxLayout(orientation='vertical',padding=10,spacing=10)
        self.lista=MDList()
        self.refresh()
        lay.add_widget(self.lista)
        btns=BoxLayout(size_hint_y=None,height=50,spacing=10)
        btns.add_widget(MDRaisedButton(text="Importa TikTok",on_release=self.importa))
        btns.add_widget(MDRaisedButton(text="Esporta x Moglie",on_release=self.esporta))
        btns.add_widget(MDRaisedButton(text="Importa da Moglie",on_release=self.importa_file))
        lay.add_widget(btns)
        return lay
    def refresh(self):
        self.lista.clear_widgets()
        con=sqlite3.connect(DB)
        for id,tit,cat in con.execute("SELECT id,titolo,categoria FROM ricette"):
            self.lista.add_widget(TwoLineAvatarIconListItem(text=tit, secondary_text=f"{cat} | Tocca per checklist", on_release=lambda x,i=id: self.apri_ricetta(i)))
        con.close()
    def importa(self,*a): print("TODO: yt-dlp + whisper")
    def apri_ricetta(self,rid): print(f"Apri {rid}")
    def esporta(self,*a):
        con=sqlite3.connect(DB)
        data={"ricette":list(con.execute("SELECT * FROM ricette")),"ingredienti":list(con.execute("SELECT * FROM ingredienti"))}
        con.close()
        open("/sdcard/Download/buio_chef_backup.json","w",encoding="utf-8").write(json.dumps(data,ensure_ascii=False))
    def importa_file(self,*a):
        data=json.load(open("/sdcard/Download/buio_chef_backup.json","r",encoding="utf-8"))
        con=sqlite3.connect(DB)
        for r in data["ricette"]: con.execute("INSERT OR IGNORE INTO ricette VALUES (?,?,?,?,?)",r)
        for i in data["ingredienti"]: con.execute("INSERT OR IGNORE INTO ingredienti VALUES (?,?,?,?,?)",i)
        con.commit(); con.close()
        self.refresh()

BuioChefApp().run()
