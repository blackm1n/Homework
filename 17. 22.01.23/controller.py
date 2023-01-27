import view as v
import module as m


def start():
    functions = [add_table_entry, remove_table_entry, update_table_entry, print_table, search_database, import_database, export_database, end]
    return functions[v.show_menu() - 1]()


def add_table_entry():
    table = v.table_options()
    if table == 1:
        return v.info(m.add_worker(v.input_worker()))
    elif table == 2:
        return v.info(m.add_position(v.input_position()))


def remove_table_entry():
    table = v.table_options()
    v.info(m.show_table(table))
    if table == 1:
        return v.info(m.delete_worker(v.input_id()))
    elif table == 2:
        return v.info(m.delete_position(v.input_id()))


def update_table_entry():
    table = v.table_options()
    v.info(m.show_table(table))
    if table == 1:
        return v.info(m.rewrite_worker(v.input_id(), v.input_worker()))
    elif table == 2:
        return v.info(m.rewrite_position(v.input_id(), v.input_position()))


def print_table():
    table = v.table_options()
    return v.info(m.show_table(table))


def search_database():
    table = v.table_options()
    criteria = 0
    key = ""
    mode = 0
    if table == 1:
        criteria = v.w_criteria_options()
        if criteria != 2:
            mode = v.search_mode()
        key = v.search_w_key(criteria)
    elif table == 2:
        criteria = v.p_criteria_options()
        if criteria == 1:
            mode = v.search_mode()
        key = v.search_p_key(criteria)
    return v.info(m.find_table_entry(table, criteria, key, mode))


def import_database():
    confirm = v.import_confirm()
    if confirm == 1:
        extension = v.extension_options()
        file_path = v.file_path()
        return v.info(m.import_file(extension, file_path))


def export_database():
    extension = v.extension_options()
    file_path = v.file_path()
    return v.info(m.export_to_file(extension, file_path))


def end():
    confirm = v.exit_confirm()
    if confirm == 1:
        return m.end_work()
