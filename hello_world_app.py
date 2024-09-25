import flet as  ft

#codigo padrão para o flet
def main(page: ft.Page):
    
        
    page.title = "Olá , mundo!"
    page.scroll = "adaptive"
    # declaração de variaveis
    nome= ft.TextField(label="Nome")
    texto ="Meu texto."
        
    page.add(
        ft.Text("Olá, mundo!",size=30,font_family="Times New Roman",color="#ffff00",weight="bold"),
        nome,
        ft.TextButton("vamos lá... "),
        ft.Text(texto)
       
        
       
    )
    
    page.update()
    
ft.app(main)   