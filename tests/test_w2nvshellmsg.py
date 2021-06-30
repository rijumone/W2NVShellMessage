import os
import pickle
import shutil
import pathlib
from w2nvshellmsg.main import (
    chk_url_up, BASE_URL,
    create_cache_dir,
    fetch, Quote,
    save_cache, CACHE_DIR,
    show_msg,
)


def test_url_working():
    """
    GIVEN nightvale fandom URL
    WHEN requested
    THEN response code is 200
    """
    assert chk_url_up(url=BASE_URL.format(pg_suff='')) == True


def test_create_cache_dir_creating_cache_dir_if_ne():
    """
    GIVEN .cache dir does or does not exist, rm if exists
    WHEN create_cache_dir() is called 
    THEN .cache dir needs to be created
    """
    try:
        shutil.rmtree(CACHE_DIR)
    except FileNotFoundError as _e:
        pass
    create_cache_dir()

    assert pathlib.Path(CACHE_DIR).is_dir() == True


def test_fetch_returns_lst():
    """
    GIVEN fetch()
    WHEN is called
    THEN should return list
    """
    return_lst = fetch()
    assert type(return_lst) == list


def test_fetch_returns_lst_item_is_Quote():
    """
    GIVEN fetch()
    WHEN is called
    THEN should return list with elements being instances of Quote
    """
    return_lst = fetch()
    assert isinstance(return_lst[0], Quote)


def test_save_cache_saves_lst_to_dir():
    """
    GIVEN save_cache()
    WHEN is called with lst arg
    THEN lst is pickled and saved to .cache
    """
    lst = fetch()
    save_cache(lst)
    chk_lst = None
    with open(os.path.join(CACHE_DIR, 'data.pkl'), 'rb') as lst_p:
        chk_lst = pickle.loads(lst_p.read())
    assert chk_lst == lst


# def test_show_msg_shows_help_if_cache_dir_ne():
#     """
#     GIVEN .cache dir does not exist, rm if exists
#     WHEN show_msg() is called
#     THEN creates .cache dir
#     """
#     assert False


def test_show_msg_shows_random_msg():
    """
    GIVEN show_msg()
    WHEN is called
    THEN message is returned
    """
    quote = show_msg(return_msg=True)
    assert type(quote.text) == str


# def test_conf_file_exists():
#     """
#     GIVEN conf.py
#     WHEN checked
#     THEN should exist
#     """
#     assert False


# def test_conf_file_color_key_exists():
#     """
#     GIVEN conf.py
#     WHEN checked
#     THEN "color" key should exist
#     """
#     assert False


# def test_conf_file_fg_bg_in_color_exists():
#     """
#     GIVEN conf.py
#     WHEN checked
#     THEN "foreground" key AND "background" key in "color" key should exist
#     """
#     assert False

# def test_show_msg_shows_random_msg_in_color_in_cnf():
#     assert False
