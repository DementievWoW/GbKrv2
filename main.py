import NoteService
import UserInterface

input_from_user = ''
while input_from_user != '7':
    UserInterface.menu()
    input_from_user = input().strip()
    if input_from_user == '1':
        NoteService.show('all')
    if input_from_user == '2':
        NoteService.add()
    if input_from_user == '3':
        NoteService.show('all')
        NoteService.id_edit_del_show('del')
    if input_from_user == '4':
        NoteService.show('all')
        NoteService.id_edit_del_show('edit')
    if input_from_user == '5':
        NoteService.show('date')
    if input_from_user == '6':
        NoteService.show('id')
        NoteService.id_edit_del_show('show')
    if input_from_user == '7':
        UserInterface.goodbuy()
