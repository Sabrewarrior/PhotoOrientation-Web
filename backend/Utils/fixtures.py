'''

    Example JSON:
    [
    {"model": "snippets.database", "pk": 0, "fields": {"name": "SUN397", "correct": false}},
    {"model": "snippets.database", "pk": 1, "fields": {"name": "SUN397", "correct": true}},
    {"model": "snippets.database", "pk": 2, "fields": {"name": "CorelDB", "correct": false}},
    {"model": "snippets.database", "pk": 3, "fields": {"name": "CorelDB", "correct": true}},
    {"model": "snippets.urllist", "pk": 1, "fields": {"db": 0, "url_orig": "images/test.jpg", "url_pos": "a",
            "url_neg": "b", "url_hot": "c", "orient": 0, "pct": 90, "pred": 2, "prob": 0}}
    ]

    ### created JSON:
    [{"model": "snippets.urllist", "pk": 0,
        "fields": {"db": 0,
                    "url_orig": "/incorrect/images/a/abbeysun_atsxxuzuiatmkwbj-orient2.jpg",
                    "url_pos": "/incorrect/images/a/abbeysun_atsxxuzuiatmkwbj-prob0-orient2pred0-pct100pos.jpg",
                    "url_neg": "/incorrect/images/a/abbeysun_atsxxuzuiatmkwbj-prob0-orient2-pred0-pct100-neg.jpg",
                    "url_hot": "/incorrect/images/a/abbeysun_atsxxuzuiatmkwbj-prob0-orient2pred0-pct100cw.jpg",
                    "orient": 2, "pct": 100, "pred": 0, "prob": 0"}}]
'''

import os

def create_db_fixtures(name_list, model_name, filename, start_pk=0):
    total_pk = len(name_list)* 2
    with open(os.path.join(os.getcwd(),filename), 'w', newline='\n') as f:
        f.write("[")
        for name in name_list:
            for x in ["false", "true"]:
                print(name)
                entry = '{"model": "' + model_name + '", "pk": ' + str(start_pk) \
                        + ', "fields": {"name": "' + name + '", "correct": ' + x + '}}'
                f.write(entry)
                start_pk += 1
                if total_pk != start_pk:
                    f.write(", ")
        f.write("]")


def create_urllist_fixtures(database_folder, model_name, inc_db_num, filename, start_pk=0):
    entry = ""
    with open(os.path.join(os.getcwd(), filename), 'w', newline='\n') as f:
        f.write("[")
        for correctness in ["incorrect", "correct"]:
            for root, folder, filenames in os.walk(os.path.join(database_folder, correctness)):
                for filename in filenames:
                    if filename.count('neg.jpg') > 0:
                        if entry == ", ":
                            f.write(entry)
                        split_name = filename.split("-")
                        prob = split_name[1].split("prob")[-1]
                        orient = split_name[2].split("orient")[-1]
                        pred = split_name[3].split("pred")[-1]
                        pct = split_name[4].split("pct")[-1]
                        url_prepend = root.replace(database_folder, '').replace('\\', '/')
                        if url_prepend[-1] != '/':
                            url_prepend = url_prepend + '/'
                        url_orig = url_prepend + split_name[0] + "-" + split_name[2] + ".jpg"
                        url_neg = url_prepend + filename
                        url_pos = url_prepend + split_name[0] + "-" + split_name[1] + "-" + split_name[2] \
                                  + "-" + split_name[3] + "-" + split_name[4] + "-pos.jpg"
                        url_hot = url_prepend + split_name[0] + "-" + split_name[1] + "-" + split_name[2] \
                                  + "-" + split_name[3] + "-" + split_name[4] + "-cw.jpg"

                        entry = '{"model": "' + model_name + '", "pk": ' + str(start_pk) \
                                + ', "fields": {"db": ' + str(inc_db_num) \
                                                + ', "url_orig": "' + url_orig \
                                                + '", "url_pos": "' + url_pos \
                                                + '", "url_neg": "' + url_neg \
                                                + '", "url_hot": "' + url_hot \
                                                + '", "orient": ' + orient \
                                                + ', "pct": ' + pct \
                                                + ', "pred": ' + pred \
                                                + ', "prob": ' + prob \
                                                + '}}'
                        f.write(entry)
                        start_pk += 1
                        entry = ", "
            inc_db_num += 1
        f.write("]")

if __name__ == "__main__":
    create_db_fixtures(["SUN397", "CorelDB"], "snippets.database", "fixtures_db.json")

    create_urllist_fixtures("D:\\PhotoOrientation\\SUN397\\gradientdesc", "snippets.urllist", 0, "fixtures_urllist.json")