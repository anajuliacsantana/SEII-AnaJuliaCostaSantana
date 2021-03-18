import os

os.chdir('/Users/anaju/Documents/Playlist')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title,f_course, f_num = f_name.split('-')
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip().zfill(2)
    #Pesquisar o atalho mostrado no vídeo
    #Alt + botaõ esquerdom mouse para selecionar
    #ctrl + shift+ alt +setas
    #fonte : https://pt.stackoverflow.com/questions/233417/sele%C3%A7%C3%A3o-multi-linha-no-vs-code#:~:text=Isso%20pode%20ser%20feito%20usando,%E2%86%92%20ou%20%E2%86%93%20ou%20%E2%86%90%20).
    new_name = '{}-{}{}'.format(f_num,f_title,f_ext)

    #os.rename(f, new_name) #deixei comentada para não alterar o arquivo novemente



