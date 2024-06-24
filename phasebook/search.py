from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!


    "return USERS"
    results = []
    added_ids=set()
    search_prio = ['id', 'name', 'age', 'occupation']

    if args != {}:
        for user in USERS:
            for key in search_prio:
                if key in args:
                    value = str(args[key])
                    user_value = str(user.get(key))

                    if str(key) == "age":
                        target_age = [int(value) + 1, int(value), int(value) - 1]
                        for age in target_age:
                            if str(age) in user_value and user['id'] not in added_ids:
                                results.append(user)
                                added_ids.add(user['id'])

                    else:
                        if value.lower() in user_value.lower() and user['id'] not in added_ids:
                            results.append(user)
                            added_ids.add(user['id'])

        return results

    else:
        return USERS



