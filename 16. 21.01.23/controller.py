import view as v
import module as m


def start():
    functions = [add_table_entry, remove_table_entry, update_table_entry, print_table, search_database, import_database, export_database, end]
    return functions[v.show_menu() - 1]()


def add_table_entry():
    table = v.table_options()
    if table == 1:
        return v.info(m.add_person(v.input_person()))
    elif table == 2:
        v.info(m.show_table(1))
        return v.info(m.add_number(v.input_number()))
    elif table == 3:
        v.info(m.show_table(1))
        return v.info(m.add_address(v.input_address()))


def remove_table_entry():
    table = v.table_options()
    v.info(m.show_table(table))
    if table == 1:
        return v.info(m.delete_person(v.input_id()))
    elif table == 2:
        return v.info(m.delete_number(v.input_id()))
    elif table == 3:
        return v.info(m.delete_address(v.input_id()))


def update_table_entry():
    table = v.table_options()
    v.info(m.show_table(table))
    if table == 1:
        return v.info(m.rewrite_person(v.input_id(), v.input_person()))
    elif table == 2:
        return v.info(m.rewrite_number(v.input_id(), v.input_number()))
    elif table == 3:
        return v.info(m.rewrite_address(v.input_id(), v.input_address()))


def print_table():
    table = v.table_options()
    return v.info(m.show_table(table))


def search_database():
    table = v.table_options()
    criteria = 0
    key = ""
    mode = 0
    if table == 1:
        criteria = v.p_criteria_options()
        if criteria == 1 or criteria == 3:
            mode = v.search_mode()
        key = v.search_p_key(criteria)
    elif table == 2:
        criteria = v.n_criteria_options()
        if criteria == 1 or criteria == 2:
            mode = v.search_mode()
        key = v.search_n_key(criteria)
    elif table == 3:
        criteria = v.a_criteria_options()
        if criteria == 1 or criteria == 2:
            mode = v.search_mode()
        key = v.search_a_key(criteria)
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
