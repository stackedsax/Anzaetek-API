# This program is a short demo of the usage of the HyperSolver API for Knapsack optimization.
# TODO add bigger examples ~ cf. benchmarks with 'A' + doc: the node version and the Julia version /=

import os
import json
import requests
from typing import cast

HYPERSOLVER_API_URL = 'https://solver.hypersolver.eu:443'
# token = os.getenv("ANZAETEK_HYPERSOLVER_TOKEN")

def solveKnapsack2(ks: dict) -> dict:
    headers = {
        'Cache-Control': 'no-cache',
        'Accept': '_/_',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive'
    }
    url = HYPERSOLVER_API_URL + '/computations/solve'
    payload= json.dumps({ "processingMethodId": "fatal-error", "knapsack": ks})
    r = requests.post(url, data=payload, headers = headers, verify=False)
    data = r.json()
    return cast(dict, data)

knapsack = {
    "version": "0.1.0",
    "name": "Knapsack 1",
    "itemCount": 1962,
    "capacity": 9766,
    "items": {
      "item-0": {
        "value": 4,
        "weight": 8
      },
      "item-1": {
        "value": 9,
        "weight": 3
      },
      "item-2": {
        "value": 6,
        "weight": 3
      },
      "item-3": {
        "value": 6,
        "weight": 3
      },
      "item-4": {
        "value": 3,
        "weight": 8
      },
      "item-5": {
        "value": 9,
        "weight": 9
      },
      "item-6": {
        "value": 3,
        "weight": 2
      },
      "item-7": {
        "value": 5,
        "weight": 3
      },
      "item-8": {
        "value": 8,
        "weight": 1
      },
      "item-9": {
        "value": 6,
        "weight": 2
      },
      "item-10": {
        "value": 3,
        "weight": 9
      },
      "item-11": {
        "value": 4,
        "weight": 2
      },
      "item-12": {
        "value": 1,
        "weight": 9
      },
      "item-13": {
        "value": 1,
        "weight": 3
      },
      "item-14": {
        "value": 3,
        "weight": 2
      },
      "item-15": {
        "value": 2,
        "weight": 4
      },
      "item-16": {
        "value": 7,
        "weight": 9
      },
      "item-17": {
        "value": 9,
        "weight": 3
      },
      "item-18": {
        "value": 1,
        "weight": 5
      },
      "item-19": {
        "value": 9,
        "weight": 4
      },
      "item-20": {
        "value": 7,
        "weight": 6
      },
      "item-21": {
        "value": 9,
        "weight": 5
      },
      "item-22": {
        "value": 4,
        "weight": 9
      },
      "item-23": {
        "value": 7,
        "weight": 4
      },
      "item-24": {
        "value": 6,
        "weight": 8
      },
      "item-25": {
        "value": 4,
        "weight": 4
      },
      "item-26": {
        "value": 8,
        "weight": 7
      },
      "item-27": {
        "value": 9,
        "weight": 9
      },
      "item-28": {
        "value": 1,
        "weight": 8
      },
      "item-29": {
        "value": 8,
        "weight": 9
      },
      "item-30": {
        "value": 9,
        "weight": 5
      },
      "item-31": {
        "value": 6,
        "weight": 7
      },
      "item-32": {
        "value": 3,
        "weight": 3
      },
      "item-33": {
        "value": 5,
        "weight": 5
      },
      "item-34": {
        "value": 1,
        "weight": 9
      },
      "item-35": {
        "value": 6,
        "weight": 3
      },
      "item-36": {
        "value": 1,
        "weight": 3
      },
      "item-37": {
        "value": 3,
        "weight": 7
      },
      "item-38": {
        "value": 5,
        "weight": 2
      },
      "item-39": {
        "value": 5,
        "weight": 1
      },
      "item-40": {
        "value": 2,
        "weight": 6
      },
      "item-41": {
        "value": 8,
        "weight": 7
      },
      "item-42": {
        "value": 8,
        "weight": 3
      },
      "item-43": {
        "value": 7,
        "weight": 9
      },
      "item-44": {
        "value": 7,
        "weight": 7
      },
      "item-45": {
        "value": 1,
        "weight": 7
      },
      "item-46": {
        "value": 6,
        "weight": 5
      },
      "item-47": {
        "value": 1,
        "weight": 3
      },
      "item-48": {
        "value": 9,
        "weight": 4
      },
      "item-49": {
        "value": 7,
        "weight": 7
      },
      "item-50": {
        "value": 8,
        "weight": 3
      },
      "item-51": {
        "value": 8,
        "weight": 8
      },
      "item-52": {
        "value": 8,
        "weight": 1
      },
      "item-53": {
        "value": 2,
        "weight": 3
      },
      "item-54": {
        "value": 4,
        "weight": 7
      },
      "item-55": {
        "value": 6,
        "weight": 9
      },
      "item-56": {
        "value": 6,
        "weight": 4
      },
      "item-57": {
        "value": 5,
        "weight": 7
      },
      "item-58": {
        "value": 8,
        "weight": 2
      },
      "item-59": {
        "value": 8,
        "weight": 9
      },
      "item-60": {
        "value": 1,
        "weight": 5
      },
      "item-61": {
        "value": 4,
        "weight": 9
      },
      "item-62": {
        "value": 2,
        "weight": 9
      },
      "item-63": {
        "value": 8,
        "weight": 3
      },
      "item-64": {
        "value": 2,
        "weight": 4
      },
      "item-65": {
        "value": 5,
        "weight": 3
      },
      "item-66": {
        "value": 9,
        "weight": 2
      },
      "item-67": {
        "value": 7,
        "weight": 6
      },
      "item-68": {
        "value": 3,
        "weight": 8
      },
      "item-69": {
        "value": 9,
        "weight": 6
      },
      "item-70": {
        "value": 1,
        "weight": 3
      },
      "item-71": {
        "value": 5,
        "weight": 1
      },
      "item-72": {
        "value": 1,
        "weight": 9
      },
      "item-73": {
        "value": 3,
        "weight": 6
      },
      "item-74": {
        "value": 7,
        "weight": 4
      },
      "item-75": {
        "value": 1,
        "weight": 9
      },
      "item-76": {
        "value": 1,
        "weight": 2
      },
      "item-77": {
        "value": 9,
        "weight": 7
      },
      "item-78": {
        "value": 4,
        "weight": 7
      },
      "item-79": {
        "value": 9,
        "weight": 2
      },
      "item-80": {
        "value": 4,
        "weight": 6
      },
      "item-81": {
        "value": 5,
        "weight": 9
      },
      "item-82": {
        "value": 4,
        "weight": 4
      },
      "item-83": {
        "value": 7,
        "weight": 6
      },
      "item-84": {
        "value": 5,
        "weight": 9
      },
      "item-85": {
        "value": 2,
        "weight": 5
      },
      "item-86": {
        "value": 1,
        "weight": 4
      },
      "item-87": {
        "value": 6,
        "weight": 5
      },
      "item-88": {
        "value": 9,
        "weight": 7
      },
      "item-89": {
        "value": 5,
        "weight": 7
      },
      "item-90": {
        "value": 7,
        "weight": 3
      },
      "item-91": {
        "value": 8,
        "weight": 4
      },
      "item-92": {
        "value": 7,
        "weight": 8
      },
      "item-93": {
        "value": 8,
        "weight": 3
      },
      "item-94": {
        "value": 8,
        "weight": 1
      },
      "item-95": {
        "value": 7,
        "weight": 9
      },
      "item-96": {
        "value": 8,
        "weight": 7
      },
      "item-97": {
        "value": 2,
        "weight": 2
      },
      "item-98": {
        "value": 3,
        "weight": 1
      },
      "item-99": {
        "value": 3,
        "weight": 5
      },
      "item-100": {
        "value": 8,
        "weight": 9
      },
      "item-101": {
        "value": 8,
        "weight": 2
      },
      "item-102": {
        "value": 8,
        "weight": 7
      },
      "item-103": {
        "value": 9,
        "weight": 8
      },
      "item-104": {
        "value": 1,
        "weight": 2
      },
      "item-105": {
        "value": 5,
        "weight": 9
      },
      "item-106": {
        "value": 8,
        "weight": 2
      },
      "item-107": {
        "value": 6,
        "weight": 7
      },
      "item-108": {
        "value": 7,
        "weight": 6
      },
      "item-109": {
        "value": 1,
        "weight": 1
      },
      "item-110": {
        "value": 1,
        "weight": 8
      },
      "item-111": {
        "value": 6,
        "weight": 8
      },
      "item-112": {
        "value": 7,
        "weight": 5
      },
      "item-113": {
        "value": 7,
        "weight": 5
      },
      "item-114": {
        "value": 6,
        "weight": 6
      },
      "item-115": {
        "value": 4,
        "weight": 4
      },
      "item-116": {
        "value": 6,
        "weight": 2
      },
      "item-117": {
        "value": 4,
        "weight": 5
      },
      "item-118": {
        "value": 6,
        "weight": 5
      },
      "item-119": {
        "value": 5,
        "weight": 8
      },
      "item-120": {
        "value": 2,
        "weight": 5
      },
      "item-121": {
        "value": 9,
        "weight": 1
      },
      "item-122": {
        "value": 3,
        "weight": 8
      },
      "item-123": {
        "value": 8,
        "weight": 4
      },
      "item-124": {
        "value": 3,
        "weight": 2
      },
      "item-125": {
        "value": 7,
        "weight": 5
      },
      "item-126": {
        "value": 8,
        "weight": 2
      },
      "item-127": {
        "value": 4,
        "weight": 5
      },
      "item-128": {
        "value": 8,
        "weight": 3
      },
      "item-129": {
        "value": 3,
        "weight": 1
      },
      "item-130": {
        "value": 3,
        "weight": 9
      },
      "item-131": {
        "value": 4,
        "weight": 9
      },
      "item-132": {
        "value": 3,
        "weight": 8
      },
      "item-133": {
        "value": 1,
        "weight": 7
      },
      "item-134": {
        "value": 1,
        "weight": 1
      },
      "item-135": {
        "value": 6,
        "weight": 4
      },
      "item-136": {
        "value": 8,
        "weight": 5
      },
      "item-137": {
        "value": 8,
        "weight": 6
      },
      "item-138": {
        "value": 4,
        "weight": 9
      },
      "item-139": {
        "value": 5,
        "weight": 8
      },
      "item-140": {
        "value": 3,
        "weight": 6
      },
      "item-141": {
        "value": 1,
        "weight": 6
      },
      "item-142": {
        "value": 2,
        "weight": 7
      },
      "item-143": {
        "value": 6,
        "weight": 7
      },
      "item-144": {
        "value": 2,
        "weight": 5
      },
      "item-145": {
        "value": 5,
        "weight": 3
      },
      "item-146": {
        "value": 1,
        "weight": 4
      },
      "item-147": {
        "value": 8,
        "weight": 8
      },
      "item-148": {
        "value": 7,
        "weight": 6
      },
      "item-149": {
        "value": 6,
        "weight": 5
      },
      "item-150": {
        "value": 3,
        "weight": 8
      },
      "item-151": {
        "value": 8,
        "weight": 5
      },
      "item-152": {
        "value": 2,
        "weight": 1
      },
      "item-153": {
        "value": 8,
        "weight": 3
      },
      "item-154": {
        "value": 2,
        "weight": 1
      },
      "item-155": {
        "value": 1,
        "weight": 8
      },
      "item-156": {
        "value": 3,
        "weight": 2
      },
      "item-157": {
        "value": 9,
        "weight": 1
      },
      "item-158": {
        "value": 4,
        "weight": 9
      },
      "item-159": {
        "value": 5,
        "weight": 6
      },
      "item-160": {
        "value": 7,
        "weight": 8
      },
      "item-161": {
        "value": 7,
        "weight": 8
      },
      "item-162": {
        "value": 8,
        "weight": 1
      },
      "item-163": {
        "value": 7,
        "weight": 5
      },
      "item-164": {
        "value": 7,
        "weight": 3
      },
      "item-165": {
        "value": 1,
        "weight": 1
      },
      "item-166": {
        "value": 7,
        "weight": 5
      },
      "item-167": {
        "value": 2,
        "weight": 8
      },
      "item-168": {
        "value": 6,
        "weight": 5
      },
      "item-169": {
        "value": 8,
        "weight": 7
      },
      "item-170": {
        "value": 8,
        "weight": 3
      },
      "item-171": {
        "value": 5,
        "weight": 7
      },
      "item-172": {
        "value": 2,
        "weight": 7
      },
      "item-173": {
        "value": 7,
        "weight": 6
      },
      "item-174": {
        "value": 3,
        "weight": 6
      },
      "item-175": {
        "value": 3,
        "weight": 9
      },
      "item-176": {
        "value": 3,
        "weight": 7
      },
      "item-177": {
        "value": 7,
        "weight": 7
      },
      "item-178": {
        "value": 8,
        "weight": 1
      },
      "item-179": {
        "value": 2,
        "weight": 3
      },
      "item-180": {
        "value": 5,
        "weight": 2
      },
      "item-181": {
        "value": 8,
        "weight": 1
      },
      "item-182": {
        "value": 1,
        "weight": 2
      },
      "item-183": {
        "value": 5,
        "weight": 6
      },
      "item-184": {
        "value": 6,
        "weight": 8
      },
      "item-185": {
        "value": 5,
        "weight": 6
      },
      "item-186": {
        "value": 5,
        "weight": 3
      },
      "item-187": {
        "value": 4,
        "weight": 8
      },
      "item-188": {
        "value": 1,
        "weight": 5
      },
      "item-189": {
        "value": 4,
        "weight": 4
      },
      "item-190": {
        "value": 8,
        "weight": 4
      },
      "item-191": {
        "value": 9,
        "weight": 9
      },
      "item-192": {
        "value": 5,
        "weight": 4
      },
      "item-193": {
        "value": 4,
        "weight": 2
      },
      "item-194": {
        "value": 7,
        "weight": 8
      },
      "item-195": {
        "value": 3,
        "weight": 1
      },
      "item-196": {
        "value": 6,
        "weight": 2
      },
      "item-197": {
        "value": 4,
        "weight": 1
      },
      "item-198": {
        "value": 3,
        "weight": 7
      },
      "item-199": {
        "value": 5,
        "weight": 3
      },
      "item-200": {
        "value": 3,
        "weight": 6
      },
      "item-201": {
        "value": 4,
        "weight": 6
      },
      "item-202": {
        "value": 9,
        "weight": 3
      },
      "item-203": {
        "value": 1,
        "weight": 9
      },
      "item-204": {
        "value": 8,
        "weight": 4
      },
      "item-205": {
        "value": 7,
        "weight": 4
      },
      "item-206": {
        "value": 7,
        "weight": 8
      },
      "item-207": {
        "value": 8,
        "weight": 7
      },
      "item-208": {
        "value": 8,
        "weight": 3
      },
      "item-209": {
        "value": 8,
        "weight": 5
      },
      "item-210": {
        "value": 6,
        "weight": 5
      },
      "item-211": {
        "value": 7,
        "weight": 1
      },
      "item-212": {
        "value": 7,
        "weight": 3
      },
      "item-213": {
        "value": 8,
        "weight": 7
      },
      "item-214": {
        "value": 6,
        "weight": 1
      },
      "item-215": {
        "value": 6,
        "weight": 1
      },
      "item-216": {
        "value": 3,
        "weight": 9
      },
      "item-217": {
        "value": 2,
        "weight": 6
      },
      "item-218": {
        "value": 5,
        "weight": 3
      },
      "item-219": {
        "value": 9,
        "weight": 9
      },
      "item-220": {
        "value": 5,
        "weight": 2
      },
      "item-221": {
        "value": 6,
        "weight": 6
      },
      "item-222": {
        "value": 5,
        "weight": 9
      },
      "item-223": {
        "value": 2,
        "weight": 5
      },
      "item-224": {
        "value": 2,
        "weight": 2
      },
      "item-225": {
        "value": 5,
        "weight": 7
      },
      "item-226": {
        "value": 4,
        "weight": 3
      },
      "item-227": {
        "value": 5,
        "weight": 5
      },
      "item-228": {
        "value": 1,
        "weight": 4
      },
      "item-229": {
        "value": 9,
        "weight": 1
      },
      "item-230": {
        "value": 4,
        "weight": 3
      },
      "item-231": {
        "value": 8,
        "weight": 6
      },
      "item-232": {
        "value": 9,
        "weight": 5
      },
      "item-233": {
        "value": 4,
        "weight": 8
      },
      "item-234": {
        "value": 5,
        "weight": 8
      },
      "item-235": {
        "value": 3,
        "weight": 5
      },
      "item-236": {
        "value": 3,
        "weight": 5
      },
      "item-237": {
        "value": 8,
        "weight": 7
      },
      "item-238": {
        "value": 6,
        "weight": 5
      },
      "item-239": {
        "value": 7,
        "weight": 1
      },
      "item-240": {
        "value": 8,
        "weight": 7
      },
      "item-241": {
        "value": 9,
        "weight": 5
      },
      "item-242": {
        "value": 1,
        "weight": 3
      },
      "item-243": {
        "value": 1,
        "weight": 1
      },
      "item-244": {
        "value": 5,
        "weight": 1
      },
      "item-245": {
        "value": 1,
        "weight": 8
      },
      "item-246": {
        "value": 1,
        "weight": 1
      },
      "item-247": {
        "value": 4,
        "weight": 7
      },
      "item-248": {
        "value": 6,
        "weight": 5
      },
      "item-249": {
        "value": 5,
        "weight": 1
      },
      "item-250": {
        "value": 4,
        "weight": 9
      },
      "item-251": {
        "value": 1,
        "weight": 3
      },
      "item-252": {
        "value": 5,
        "weight": 9
      },
      "item-253": {
        "value": 6,
        "weight": 5
      },
      "item-254": {
        "value": 2,
        "weight": 9
      },
      "item-255": {
        "value": 4,
        "weight": 3
      },
      "item-256": {
        "value": 8,
        "weight": 6
      },
      "item-257": {
        "value": 6,
        "weight": 9
      },
      "item-258": {
        "value": 4,
        "weight": 3
      },
      "item-259": {
        "value": 2,
        "weight": 8
      },
      "item-260": {
        "value": 8,
        "weight": 5
      },
      "item-261": {
        "value": 6,
        "weight": 8
      },
      "item-262": {
        "value": 3,
        "weight": 9
      },
      "item-263": {
        "value": 8,
        "weight": 2
      },
      "item-264": {
        "value": 2,
        "weight": 9
      },
      "item-265": {
        "value": 3,
        "weight": 2
      },
      "item-266": {
        "value": 4,
        "weight": 4
      },
      "item-267": {
        "value": 6,
        "weight": 1
      },
      "item-268": {
        "value": 4,
        "weight": 1
      },
      "item-269": {
        "value": 1,
        "weight": 6
      },
      "item-270": {
        "value": 7,
        "weight": 5
      },
      "item-271": {
        "value": 8,
        "weight": 6
      },
      "item-272": {
        "value": 3,
        "weight": 7
      },
      "item-273": {
        "value": 9,
        "weight": 3
      },
      "item-274": {
        "value": 6,
        "weight": 1
      },
      "item-275": {
        "value": 9,
        "weight": 5
      },
      "item-276": {
        "value": 3,
        "weight": 5
      },
      "item-277": {
        "value": 4,
        "weight": 1
      },
      "item-278": {
        "value": 1,
        "weight": 9
      },
      "item-279": {
        "value": 6,
        "weight": 8
      },
      "item-280": {
        "value": 6,
        "weight": 3
      },
      "item-281": {
        "value": 9,
        "weight": 4
      },
      "item-282": {
        "value": 3,
        "weight": 2
      },
      "item-283": {
        "value": 6,
        "weight": 8
      },
      "item-284": {
        "value": 4,
        "weight": 4
      },
      "item-285": {
        "value": 3,
        "weight": 9
      },
      "item-286": {
        "value": 1,
        "weight": 9
      },
      "item-287": {
        "value": 5,
        "weight": 5
      },
      "item-288": {
        "value": 7,
        "weight": 2
      },
      "item-289": {
        "value": 4,
        "weight": 1
      },
      "item-290": {
        "value": 2,
        "weight": 3
      },
      "item-291": {
        "value": 1,
        "weight": 5
      },
      "item-292": {
        "value": 3,
        "weight": 4
      },
      "item-293": {
        "value": 6,
        "weight": 5
      },
      "item-294": {
        "value": 5,
        "weight": 8
      },
      "item-295": {
        "value": 2,
        "weight": 3
      },
      "item-296": {
        "value": 5,
        "weight": 7
      },
      "item-297": {
        "value": 6,
        "weight": 8
      },
      "item-298": {
        "value": 6,
        "weight": 2
      },
      "item-299": {
        "value": 8,
        "weight": 8
      },
      "item-300": {
        "value": 9,
        "weight": 8
      },
      "item-301": {
        "value": 5,
        "weight": 3
      },
      "item-302": {
        "value": 4,
        "weight": 3
      },
      "item-303": {
        "value": 2,
        "weight": 1
      },
      "item-304": {
        "value": 4,
        "weight": 4
      },
      "item-305": {
        "value": 7,
        "weight": 1
      },
      "item-306": {
        "value": 1,
        "weight": 9
      },
      "item-307": {
        "value": 1,
        "weight": 9
      },
      "item-308": {
        "value": 3,
        "weight": 1
      },
      "item-309": {
        "value": 9,
        "weight": 4
      },
      "item-310": {
        "value": 5,
        "weight": 9
      },
      "item-311": {
        "value": 5,
        "weight": 9
      },
      "item-312": {
        "value": 7,
        "weight": 5
      },
      "item-313": {
        "value": 5,
        "weight": 1
      },
      "item-314": {
        "value": 6,
        "weight": 6
      },
      "item-315": {
        "value": 2,
        "weight": 2
      },
      "item-316": {
        "value": 8,
        "weight": 9
      },
      "item-317": {
        "value": 6,
        "weight": 7
      },
      "item-318": {
        "value": 2,
        "weight": 6
      },
      "item-319": {
        "value": 4,
        "weight": 5
      },
      "item-320": {
        "value": 3,
        "weight": 5
      },
      "item-321": {
        "value": 6,
        "weight": 4
      },
      "item-322": {
        "value": 4,
        "weight": 9
      },
      "item-323": {
        "value": 9,
        "weight": 4
      },
      "item-324": {
        "value": 8,
        "weight": 3
      },
      "item-325": {
        "value": 1,
        "weight": 2
      },
      "item-326": {
        "value": 8,
        "weight": 3
      },
      "item-327": {
        "value": 2,
        "weight": 4
      },
      "item-328": {
        "value": 1,
        "weight": 5
      },
      "item-329": {
        "value": 7,
        "weight": 9
      },
      "item-330": {
        "value": 2,
        "weight": 2
      },
      "item-331": {
        "value": 8,
        "weight": 1
      },
      "item-332": {
        "value": 1,
        "weight": 3
      },
      "item-333": {
        "value": 5,
        "weight": 4
      },
      "item-334": {
        "value": 1,
        "weight": 2
      },
      "item-335": {
        "value": 2,
        "weight": 8
      },
      "item-336": {
        "value": 5,
        "weight": 1
      },
      "item-337": {
        "value": 8,
        "weight": 2
      },
      "item-338": {
        "value": 1,
        "weight": 2
      },
      "item-339": {
        "value": 4,
        "weight": 5
      },
      "item-340": {
        "value": 2,
        "weight": 1
      },
      "item-341": {
        "value": 4,
        "weight": 6
      },
      "item-342": {
        "value": 8,
        "weight": 3
      },
      "item-343": {
        "value": 5,
        "weight": 3
      },
      "item-344": {
        "value": 8,
        "weight": 2
      },
      "item-345": {
        "value": 2,
        "weight": 4
      },
      "item-346": {
        "value": 3,
        "weight": 4
      },
      "item-347": {
        "value": 8,
        "weight": 8
      },
      "item-348": {
        "value": 4,
        "weight": 5
      },
      "item-349": {
        "value": 4,
        "weight": 2
      },
      "item-350": {
        "value": 7,
        "weight": 9
      },
      "item-351": {
        "value": 9,
        "weight": 3
      },
      "item-352": {
        "value": 4,
        "weight": 1
      },
      "item-353": {
        "value": 2,
        "weight": 3
      },
      "item-354": {
        "value": 6,
        "weight": 7
      },
      "item-355": {
        "value": 9,
        "weight": 7
      },
      "item-356": {
        "value": 5,
        "weight": 2
      },
      "item-357": {
        "value": 6,
        "weight": 8
      },
      "item-358": {
        "value": 5,
        "weight": 1
      },
      "item-359": {
        "value": 2,
        "weight": 9
      },
      "item-360": {
        "value": 7,
        "weight": 4
      },
      "item-361": {
        "value": 7,
        "weight": 7
      },
      "item-362": {
        "value": 6,
        "weight": 9
      },
      "item-363": {
        "value": 3,
        "weight": 1
      },
      "item-364": {
        "value": 2,
        "weight": 4
      },
      "item-365": {
        "value": 5,
        "weight": 8
      },
      "item-366": {
        "value": 8,
        "weight": 3
      },
      "item-367": {
        "value": 8,
        "weight": 9
      },
      "item-368": {
        "value": 9,
        "weight": 3
      },
      "item-369": {
        "value": 4,
        "weight": 5
      },
      "item-370": {
        "value": 7,
        "weight": 9
      },
      "item-371": {
        "value": 3,
        "weight": 8
      },
      "item-372": {
        "value": 1,
        "weight": 6
      },
      "item-373": {
        "value": 4,
        "weight": 9
      },
      "item-374": {
        "value": 2,
        "weight": 6
      },
      "item-375": {
        "value": 5,
        "weight": 8
      },
      "item-376": {
        "value": 2,
        "weight": 1
      },
      "item-377": {
        "value": 6,
        "weight": 9
      },
      "item-378": {
        "value": 4,
        "weight": 1
      },
      "item-379": {
        "value": 4,
        "weight": 4
      },
      "item-380": {
        "value": 1,
        "weight": 2
      },
      "item-381": {
        "value": 1,
        "weight": 6
      },
      "item-382": {
        "value": 7,
        "weight": 1
      },
      "item-383": {
        "value": 9,
        "weight": 7
      },
      "item-384": {
        "value": 9,
        "weight": 5
      },
      "item-385": {
        "value": 8,
        "weight": 1
      },
      "item-386": {
        "value": 3,
        "weight": 6
      },
      "item-387": {
        "value": 1,
        "weight": 5
      },
      "item-388": {
        "value": 1,
        "weight": 9
      },
      "item-389": {
        "value": 7,
        "weight": 1
      },
      "item-390": {
        "value": 6,
        "weight": 1
      },
      "item-391": {
        "value": 3,
        "weight": 9
      },
      "item-392": {
        "value": 4,
        "weight": 2
      },
      "item-393": {
        "value": 3,
        "weight": 3
      },
      "item-394": {
        "value": 8,
        "weight": 4
      },
      "item-395": {
        "value": 7,
        "weight": 1
      },
      "item-396": {
        "value": 5,
        "weight": 2
      },
      "item-397": {
        "value": 2,
        "weight": 8
      },
      "item-398": {
        "value": 2,
        "weight": 4
      },
      "item-399": {
        "value": 4,
        "weight": 8
      },
      "item-400": {
        "value": 3,
        "weight": 5
      },
      "item-401": {
        "value": 1,
        "weight": 3
      },
      "item-402": {
        "value": 7,
        "weight": 1
      },
      "item-403": {
        "value": 2,
        "weight": 6
      },
      "item-404": {
        "value": 9,
        "weight": 9
      },
      "item-405": {
        "value": 9,
        "weight": 9
      },
      "item-406": {
        "value": 8,
        "weight": 9
      },
      "item-407": {
        "value": 1,
        "weight": 4
      },
      "item-408": {
        "value": 1,
        "weight": 7
      },
      "item-409": {
        "value": 4,
        "weight": 5
      },
      "item-410": {
        "value": 9,
        "weight": 8
      },
      "item-411": {
        "value": 6,
        "weight": 3
      },
      "item-412": {
        "value": 4,
        "weight": 9
      },
      "item-413": {
        "value": 7,
        "weight": 3
      },
      "item-414": {
        "value": 2,
        "weight": 4
      },
      "item-415": {
        "value": 3,
        "weight": 4
      },
      "item-416": {
        "value": 2,
        "weight": 1
      },
      "item-417": {
        "value": 1,
        "weight": 2
      },
      "item-418": {
        "value": 7,
        "weight": 3
      },
      "item-419": {
        "value": 2,
        "weight": 7
      },
      "item-420": {
        "value": 9,
        "weight": 8
      },
      "item-421": {
        "value": 5,
        "weight": 5
      },
      "item-422": {
        "value": 9,
        "weight": 4
      },
      "item-423": {
        "value": 9,
        "weight": 3
      },
      "item-424": {
        "value": 1,
        "weight": 2
      },
      "item-425": {
        "value": 3,
        "weight": 4
      },
      "item-426": {
        "value": 6,
        "weight": 9
      },
      "item-427": {
        "value": 6,
        "weight": 4
      },
      "item-428": {
        "value": 3,
        "weight": 7
      },
      "item-429": {
        "value": 8,
        "weight": 7
      },
      "item-430": {
        "value": 7,
        "weight": 6
      },
      "item-431": {
        "value": 5,
        "weight": 5
      },
      "item-432": {
        "value": 9,
        "weight": 8
      },
      "item-433": {
        "value": 1,
        "weight": 4
      },
      "item-434": {
        "value": 7,
        "weight": 5
      },
      "item-435": {
        "value": 3,
        "weight": 2
      },
      "item-436": {
        "value": 3,
        "weight": 8
      },
      "item-437": {
        "value": 3,
        "weight": 5
      },
      "item-438": {
        "value": 8,
        "weight": 9
      },
      "item-439": {
        "value": 5,
        "weight": 2
      },
      "item-440": {
        "value": 2,
        "weight": 7
      },
      "item-441": {
        "value": 7,
        "weight": 1
      },
      "item-442": {
        "value": 1,
        "weight": 6
      },
      "item-443": {
        "value": 2,
        "weight": 5
      },
      "item-444": {
        "value": 9,
        "weight": 8
      },
      "item-445": {
        "value": 3,
        "weight": 6
      },
      "item-446": {
        "value": 5,
        "weight": 2
      },
      "item-447": {
        "value": 7,
        "weight": 4
      },
      "item-448": {
        "value": 3,
        "weight": 2
      },
      "item-449": {
        "value": 4,
        "weight": 1
      },
      "item-450": {
        "value": 9,
        "weight": 6
      },
      "item-451": {
        "value": 7,
        "weight": 5
      },
      "item-452": {
        "value": 7,
        "weight": 2
      },
      "item-453": {
        "value": 4,
        "weight": 7
      },
      "item-454": {
        "value": 1,
        "weight": 8
      },
      "item-455": {
        "value": 9,
        "weight": 7
      },
      "item-456": {
        "value": 2,
        "weight": 5
      },
      "item-457": {
        "value": 5,
        "weight": 8
      },
      "item-458": {
        "value": 1,
        "weight": 6
      },
      "item-459": {
        "value": 8,
        "weight": 5
      },
      "item-460": {
        "value": 7,
        "weight": 5
      },
      "item-461": {
        "value": 3,
        "weight": 7
      },
      "item-462": {
        "value": 4,
        "weight": 6
      },
      "item-463": {
        "value": 4,
        "weight": 2
      },
      "item-464": {
        "value": 1,
        "weight": 8
      },
      "item-465": {
        "value": 7,
        "weight": 8
      },
      "item-466": {
        "value": 4,
        "weight": 9
      },
      "item-467": {
        "value": 7,
        "weight": 2
      },
      "item-468": {
        "value": 6,
        "weight": 3
      },
      "item-469": {
        "value": 7,
        "weight": 4
      },
      "item-470": {
        "value": 4,
        "weight": 7
      },
      "item-471": {
        "value": 9,
        "weight": 2
      },
      "item-472": {
        "value": 6,
        "weight": 8
      },
      "item-473": {
        "value": 9,
        "weight": 3
      },
      "item-474": {
        "value": 1,
        "weight": 4
      },
      "item-475": {
        "value": 9,
        "weight": 9
      },
      "item-476": {
        "value": 9,
        "weight": 6
      },
      "item-477": {
        "value": 5,
        "weight": 5
      },
      "item-478": {
        "value": 6,
        "weight": 8
      },
      "item-479": {
        "value": 4,
        "weight": 4
      },
      "item-480": {
        "value": 1,
        "weight": 1
      },
      "item-481": {
        "value": 5,
        "weight": 2
      },
      "item-482": {
        "value": 6,
        "weight": 1
      },
      "item-483": {
        "value": 8,
        "weight": 9
      },
      "item-484": {
        "value": 5,
        "weight": 6
      },
      "item-485": {
        "value": 9,
        "weight": 1
      },
      "item-486": {
        "value": 3,
        "weight": 2
      },
      "item-487": {
        "value": 6,
        "weight": 6
      },
      "item-488": {
        "value": 1,
        "weight": 2
      },
      "item-489": {
        "value": 9,
        "weight": 9
      },
      "item-490": {
        "value": 5,
        "weight": 5
      },
      "item-491": {
        "value": 4,
        "weight": 1
      },
      "item-492": {
        "value": 3,
        "weight": 1
      },
      "item-493": {
        "value": 8,
        "weight": 3
      },
      "item-494": {
        "value": 1,
        "weight": 9
      },
      "item-495": {
        "value": 7,
        "weight": 3
      },
      "item-496": {
        "value": 6,
        "weight": 9
      },
      "item-497": {
        "value": 9,
        "weight": 8
      },
      "item-498": {
        "value": 3,
        "weight": 1
      },
      "item-499": {
        "value": 4,
        "weight": 6
      },
      "item-500": {
        "value": 1,
        "weight": 3
      },
      "item-501": {
        "value": 9,
        "weight": 4
      },
      "item-502": {
        "value": 6,
        "weight": 1
      },
      "item-503": {
        "value": 7,
        "weight": 4
      },
      "item-504": {
        "value": 5,
        "weight": 2
      },
      "item-505": {
        "value": 2,
        "weight": 2
      },
      "item-506": {
        "value": 2,
        "weight": 6
      },
      "item-507": {
        "value": 1,
        "weight": 5
      },
      "item-508": {
        "value": 7,
        "weight": 5
      },
      "item-509": {
        "value": 5,
        "weight": 8
      },
      "item-510": {
        "value": 1,
        "weight": 1
      },
      "item-511": {
        "value": 5,
        "weight": 9
      },
      "item-512": {
        "value": 3,
        "weight": 7
      },
      "item-513": {
        "value": 6,
        "weight": 9
      },
      "item-514": {
        "value": 7,
        "weight": 5
      },
      "item-515": {
        "value": 4,
        "weight": 2
      },
      "item-516": {
        "value": 8,
        "weight": 2
      },
      "item-517": {
        "value": 8,
        "weight": 8
      },
      "item-518": {
        "value": 5,
        "weight": 2
      },
      "item-519": {
        "value": 6,
        "weight": 3
      },
      "item-520": {
        "value": 6,
        "weight": 8
      },
      "item-521": {
        "value": 5,
        "weight": 6
      },
      "item-522": {
        "value": 9,
        "weight": 5
      },
      "item-523": {
        "value": 5,
        "weight": 9
      },
      "item-524": {
        "value": 1,
        "weight": 8
      },
      "item-525": {
        "value": 7,
        "weight": 7
      },
      "item-526": {
        "value": 9,
        "weight": 8
      },
      "item-527": {
        "value": 1,
        "weight": 8
      },
      "item-528": {
        "value": 4,
        "weight": 3
      },
      "item-529": {
        "value": 3,
        "weight": 4
      },
      "item-530": {
        "value": 4,
        "weight": 3
      },
      "item-531": {
        "value": 4,
        "weight": 1
      },
      "item-532": {
        "value": 7,
        "weight": 2
      },
      "item-533": {
        "value": 3,
        "weight": 9
      },
      "item-534": {
        "value": 1,
        "weight": 1
      },
      "item-535": {
        "value": 9,
        "weight": 9
      },
      "item-536": {
        "value": 1,
        "weight": 5
      },
      "item-537": {
        "value": 4,
        "weight": 2
      },
      "item-538": {
        "value": 2,
        "weight": 6
      },
      "item-539": {
        "value": 5,
        "weight": 2
      },
      "item-540": {
        "value": 2,
        "weight": 8
      },
      "item-541": {
        "value": 9,
        "weight": 7
      },
      "item-542": {
        "value": 5,
        "weight": 6
      },
      "item-543": {
        "value": 3,
        "weight": 4
      },
      "item-544": {
        "value": 9,
        "weight": 8
      },
      "item-545": {
        "value": 3,
        "weight": 9
      },
      "item-546": {
        "value": 8,
        "weight": 1
      },
      "item-547": {
        "value": 5,
        "weight": 4
      },
      "item-548": {
        "value": 4,
        "weight": 3
      },
      "item-549": {
        "value": 5,
        "weight": 9
      },
      "item-550": {
        "value": 9,
        "weight": 3
      },
      "item-551": {
        "value": 8,
        "weight": 2
      },
      "item-552": {
        "value": 3,
        "weight": 7
      },
      "item-553": {
        "value": 8,
        "weight": 9
      },
      "item-554": {
        "value": 6,
        "weight": 4
      },
      "item-555": {
        "value": 4,
        "weight": 8
      },
      "item-556": {
        "value": 8,
        "weight": 7
      },
      "item-557": {
        "value": 3,
        "weight": 8
      },
      "item-558": {
        "value": 8,
        "weight": 9
      },
      "item-559": {
        "value": 8,
        "weight": 7
      },
      "item-560": {
        "value": 6,
        "weight": 1
      },
      "item-561": {
        "value": 9,
        "weight": 9
      },
      "item-562": {
        "value": 7,
        "weight": 8
      },
      "item-563": {
        "value": 2,
        "weight": 3
      },
      "item-564": {
        "value": 7,
        "weight": 7
      },
      "item-565": {
        "value": 3,
        "weight": 4
      },
      "item-566": {
        "value": 2,
        "weight": 9
      },
      "item-567": {
        "value": 5,
        "weight": 2
      },
      "item-568": {
        "value": 5,
        "weight": 8
      },
      "item-569": {
        "value": 7,
        "weight": 1
      },
      "item-570": {
        "value": 2,
        "weight": 5
      },
      "item-571": {
        "value": 4,
        "weight": 3
      },
      "item-572": {
        "value": 2,
        "weight": 2
      },
      "item-573": {
        "value": 4,
        "weight": 5
      },
      "item-574": {
        "value": 1,
        "weight": 8
      },
      "item-575": {
        "value": 6,
        "weight": 9
      },
      "item-576": {
        "value": 3,
        "weight": 6
      },
      "item-577": {
        "value": 9,
        "weight": 5
      },
      "item-578": {
        "value": 7,
        "weight": 9
      },
      "item-579": {
        "value": 1,
        "weight": 2
      },
      "item-580": {
        "value": 8,
        "weight": 9
      },
      "item-581": {
        "value": 2,
        "weight": 2
      },
      "item-582": {
        "value": 7,
        "weight": 6
      },
      "item-583": {
        "value": 8,
        "weight": 5
      },
      "item-584": {
        "value": 8,
        "weight": 8
      },
      "item-585": {
        "value": 1,
        "weight": 6
      },
      "item-586": {
        "value": 1,
        "weight": 5
      },
      "item-587": {
        "value": 1,
        "weight": 8
      },
      "item-588": {
        "value": 4,
        "weight": 6
      },
      "item-589": {
        "value": 2,
        "weight": 9
      },
      "item-590": {
        "value": 3,
        "weight": 3
      },
      "item-591": {
        "value": 7,
        "weight": 1
      },
      "item-592": {
        "value": 3,
        "weight": 4
      },
      "item-593": {
        "value": 2,
        "weight": 9
      },
      "item-594": {
        "value": 2,
        "weight": 2
      },
      "item-595": {
        "value": 8,
        "weight": 4
      },
      "item-596": {
        "value": 5,
        "weight": 2
      },
      "item-597": {
        "value": 7,
        "weight": 5
      },
      "item-598": {
        "value": 4,
        "weight": 2
      },
      "item-599": {
        "value": 2,
        "weight": 5
      },
      "item-600": {
        "value": 3,
        "weight": 8
      },
      "item-601": {
        "value": 8,
        "weight": 5
      },
      "item-602": {
        "value": 9,
        "weight": 1
      },
      "item-603": {
        "value": 4,
        "weight": 3
      },
      "item-604": {
        "value": 2,
        "weight": 3
      },
      "item-605": {
        "value": 9,
        "weight": 3
      },
      "item-606": {
        "value": 9,
        "weight": 4
      },
      "item-607": {
        "value": 4,
        "weight": 4
      },
      "item-608": {
        "value": 2,
        "weight": 5
      },
      "item-609": {
        "value": 1,
        "weight": 5
      },
      "item-610": {
        "value": 8,
        "weight": 3
      },
      "item-611": {
        "value": 2,
        "weight": 6
      },
      "item-612": {
        "value": 8,
        "weight": 1
      },
      "item-613": {
        "value": 1,
        "weight": 7
      },
      "item-614": {
        "value": 2,
        "weight": 1
      },
      "item-615": {
        "value": 1,
        "weight": 5
      },
      "item-616": {
        "value": 3,
        "weight": 3
      },
      "item-617": {
        "value": 3,
        "weight": 6
      },
      "item-618": {
        "value": 5,
        "weight": 6
      },
      "item-619": {
        "value": 6,
        "weight": 1
      },
      "item-620": {
        "value": 7,
        "weight": 3
      },
      "item-621": {
        "value": 4,
        "weight": 7
      },
      "item-622": {
        "value": 7,
        "weight": 4
      },
      "item-623": {
        "value": 4,
        "weight": 7
      },
      "item-624": {
        "value": 1,
        "weight": 2
      },
      "item-625": {
        "value": 5,
        "weight": 9
      },
      "item-626": {
        "value": 5,
        "weight": 9
      },
      "item-627": {
        "value": 9,
        "weight": 1
      },
      "item-628": {
        "value": 4,
        "weight": 1
      },
      "item-629": {
        "value": 3,
        "weight": 5
      },
      "item-630": {
        "value": 8,
        "weight": 5
      },
      "item-631": {
        "value": 1,
        "weight": 6
      },
      "item-632": {
        "value": 8,
        "weight": 6
      },
      "item-633": {
        "value": 4,
        "weight": 1
      },
      "item-634": {
        "value": 6,
        "weight": 4
      },
      "item-635": {
        "value": 3,
        "weight": 1
      },
      "item-636": {
        "value": 2,
        "weight": 6
      },
      "item-637": {
        "value": 1,
        "weight": 7
      },
      "item-638": {
        "value": 5,
        "weight": 1
      },
      "item-639": {
        "value": 7,
        "weight": 2
      },
      "item-640": {
        "value": 4,
        "weight": 7
      },
      "item-641": {
        "value": 1,
        "weight": 9
      },
      "item-642": {
        "value": 7,
        "weight": 3
      },
      "item-643": {
        "value": 1,
        "weight": 6
      },
      "item-644": {
        "value": 3,
        "weight": 3
      },
      "item-645": {
        "value": 7,
        "weight": 8
      },
      "item-646": {
        "value": 1,
        "weight": 7
      },
      "item-647": {
        "value": 3,
        "weight": 9
      },
      "item-648": {
        "value": 8,
        "weight": 4
      },
      "item-649": {
        "value": 7,
        "weight": 3
      },
      "item-650": {
        "value": 9,
        "weight": 3
      },
      "item-651": {
        "value": 6,
        "weight": 2
      },
      "item-652": {
        "value": 7,
        "weight": 2
      },
      "item-653": {
        "value": 4,
        "weight": 5
      },
      "item-654": {
        "value": 6,
        "weight": 4
      },
      "item-655": {
        "value": 7,
        "weight": 7
      },
      "item-656": {
        "value": 9,
        "weight": 7
      },
      "item-657": {
        "value": 5,
        "weight": 9
      },
      "item-658": {
        "value": 7,
        "weight": 4
      },
      "item-659": {
        "value": 9,
        "weight": 4
      },
      "item-660": {
        "value": 4,
        "weight": 2
      },
      "item-661": {
        "value": 2,
        "weight": 5
      },
      "item-662": {
        "value": 7,
        "weight": 2
      },
      "item-663": {
        "value": 5,
        "weight": 8
      },
      "item-664": {
        "value": 8,
        "weight": 2
      },
      "item-665": {
        "value": 6,
        "weight": 4
      },
      "item-666": {
        "value": 4,
        "weight": 9
      },
      "item-667": {
        "value": 2,
        "weight": 1
      },
      "item-668": {
        "value": 3,
        "weight": 3
      },
      "item-669": {
        "value": 4,
        "weight": 9
      },
      "item-670": {
        "value": 9,
        "weight": 4
      },
      "item-671": {
        "value": 4,
        "weight": 2
      },
      "item-672": {
        "value": 2,
        "weight": 9
      },
      "item-673": {
        "value": 4,
        "weight": 4
      },
      "item-674": {
        "value": 6,
        "weight": 5
      },
      "item-675": {
        "value": 2,
        "weight": 9
      },
      "item-676": {
        "value": 7,
        "weight": 6
      },
      "item-677": {
        "value": 5,
        "weight": 5
      },
      "item-678": {
        "value": 9,
        "weight": 7
      },
      "item-679": {
        "value": 3,
        "weight": 8
      },
      "item-680": {
        "value": 7,
        "weight": 8
      },
      "item-681": {
        "value": 6,
        "weight": 9
      },
      "item-682": {
        "value": 4,
        "weight": 2
      },
      "item-683": {
        "value": 2,
        "weight": 4
      },
      "item-684": {
        "value": 9,
        "weight": 5
      },
      "item-685": {
        "value": 6,
        "weight": 8
      },
      "item-686": {
        "value": 7,
        "weight": 3
      },
      "item-687": {
        "value": 6,
        "weight": 3
      },
      "item-688": {
        "value": 6,
        "weight": 8
      },
      "item-689": {
        "value": 1,
        "weight": 5
      },
      "item-690": {
        "value": 6,
        "weight": 3
      },
      "item-691": {
        "value": 9,
        "weight": 8
      },
      "item-692": {
        "value": 9,
        "weight": 8
      },
      "item-693": {
        "value": 1,
        "weight": 8
      },
      "item-694": {
        "value": 3,
        "weight": 1
      },
      "item-695": {
        "value": 6,
        "weight": 4
      },
      "item-696": {
        "value": 7,
        "weight": 4
      },
      "item-697": {
        "value": 6,
        "weight": 5
      },
      "item-698": {
        "value": 2,
        "weight": 1
      },
      "item-699": {
        "value": 3,
        "weight": 6
      },
      "item-700": {
        "value": 9,
        "weight": 2
      },
      "item-701": {
        "value": 5,
        "weight": 1
      },
      "item-702": {
        "value": 4,
        "weight": 2
      },
      "item-703": {
        "value": 1,
        "weight": 5
      },
      "item-704": {
        "value": 8,
        "weight": 5
      },
      "item-705": {
        "value": 4,
        "weight": 2
      },
      "item-706": {
        "value": 7,
        "weight": 3
      },
      "item-707": {
        "value": 5,
        "weight": 6
      },
      "item-708": {
        "value": 2,
        "weight": 9
      },
      "item-709": {
        "value": 9,
        "weight": 8
      },
      "item-710": {
        "value": 1,
        "weight": 6
      },
      "item-711": {
        "value": 1,
        "weight": 5
      },
      "item-712": {
        "value": 9,
        "weight": 1
      },
      "item-713": {
        "value": 3,
        "weight": 5
      },
      "item-714": {
        "value": 1,
        "weight": 6
      },
      "item-715": {
        "value": 8,
        "weight": 1
      },
      "item-716": {
        "value": 3,
        "weight": 9
      },
      "item-717": {
        "value": 2,
        "weight": 5
      },
      "item-718": {
        "value": 6,
        "weight": 1
      },
      "item-719": {
        "value": 5,
        "weight": 9
      },
      "item-720": {
        "value": 8,
        "weight": 2
      },
      "item-721": {
        "value": 1,
        "weight": 2
      },
      "item-722": {
        "value": 5,
        "weight": 9
      },
      "item-723": {
        "value": 2,
        "weight": 8
      },
      "item-724": {
        "value": 6,
        "weight": 6
      },
      "item-725": {
        "value": 3,
        "weight": 5
      },
      "item-726": {
        "value": 2,
        "weight": 5
      },
      "item-727": {
        "value": 8,
        "weight": 5
      },
      "item-728": {
        "value": 2,
        "weight": 7
      },
      "item-729": {
        "value": 8,
        "weight": 3
      },
      "item-730": {
        "value": 4,
        "weight": 7
      },
      "item-731": {
        "value": 4,
        "weight": 2
      },
      "item-732": {
        "value": 9,
        "weight": 6
      },
      "item-733": {
        "value": 3,
        "weight": 5
      },
      "item-734": {
        "value": 1,
        "weight": 6
      },
      "item-735": {
        "value": 6,
        "weight": 5
      },
      "item-736": {
        "value": 7,
        "weight": 8
      },
      "item-737": {
        "value": 4,
        "weight": 3
      },
      "item-738": {
        "value": 9,
        "weight": 7
      },
      "item-739": {
        "value": 9,
        "weight": 8
      },
      "item-740": {
        "value": 6,
        "weight": 9
      },
      "item-741": {
        "value": 2,
        "weight": 9
      },
      "item-742": {
        "value": 5,
        "weight": 5
      },
      "item-743": {
        "value": 2,
        "weight": 3
      },
      "item-744": {
        "value": 6,
        "weight": 6
      },
      "item-745": {
        "value": 8,
        "weight": 2
      },
      "item-746": {
        "value": 5,
        "weight": 7
      },
      "item-747": {
        "value": 7,
        "weight": 7
      },
      "item-748": {
        "value": 6,
        "weight": 7
      },
      "item-749": {
        "value": 2,
        "weight": 2
      },
      "item-750": {
        "value": 1,
        "weight": 9
      },
      "item-751": {
        "value": 6,
        "weight": 2
      },
      "item-752": {
        "value": 7,
        "weight": 2
      },
      "item-753": {
        "value": 1,
        "weight": 7
      },
      "item-754": {
        "value": 9,
        "weight": 6
      },
      "item-755": {
        "value": 6,
        "weight": 3
      },
      "item-756": {
        "value": 4,
        "weight": 7
      },
      "item-757": {
        "value": 4,
        "weight": 2
      },
      "item-758": {
        "value": 5,
        "weight": 9
      },
      "item-759": {
        "value": 2,
        "weight": 9
      },
      "item-760": {
        "value": 4,
        "weight": 6
      },
      "item-761": {
        "value": 9,
        "weight": 5
      },
      "item-762": {
        "value": 1,
        "weight": 1
      },
      "item-763": {
        "value": 4,
        "weight": 2
      },
      "item-764": {
        "value": 6,
        "weight": 1
      },
      "item-765": {
        "value": 7,
        "weight": 2
      },
      "item-766": {
        "value": 9,
        "weight": 5
      },
      "item-767": {
        "value": 1,
        "weight": 9
      },
      "item-768": {
        "value": 5,
        "weight": 6
      },
      "item-769": {
        "value": 2,
        "weight": 8
      },
      "item-770": {
        "value": 6,
        "weight": 5
      },
      "item-771": {
        "value": 3,
        "weight": 5
      },
      "item-772": {
        "value": 6,
        "weight": 9
      },
      "item-773": {
        "value": 8,
        "weight": 7
      },
      "item-774": {
        "value": 5,
        "weight": 3
      },
      "item-775": {
        "value": 4,
        "weight": 9
      },
      "item-776": {
        "value": 4,
        "weight": 1
      },
      "item-777": {
        "value": 7,
        "weight": 2
      },
      "item-778": {
        "value": 9,
        "weight": 2
      },
      "item-779": {
        "value": 1,
        "weight": 2
      },
      "item-780": {
        "value": 7,
        "weight": 9
      },
      "item-781": {
        "value": 9,
        "weight": 2
      },
      "item-782": {
        "value": 1,
        "weight": 9
      },
      "item-783": {
        "value": 5,
        "weight": 7
      },
      "item-784": {
        "value": 3,
        "weight": 8
      },
      "item-785": {
        "value": 5,
        "weight": 7
      },
      "item-786": {
        "value": 3,
        "weight": 6
      },
      "item-787": {
        "value": 1,
        "weight": 5
      },
      "item-788": {
        "value": 3,
        "weight": 5
      },
      "item-789": {
        "value": 8,
        "weight": 9
      },
      "item-790": {
        "value": 2,
        "weight": 5
      },
      "item-791": {
        "value": 1,
        "weight": 1
      },
      "item-792": {
        "value": 3,
        "weight": 8
      },
      "item-793": {
        "value": 4,
        "weight": 9
      },
      "item-794": {
        "value": 7,
        "weight": 8
      },
      "item-795": {
        "value": 1,
        "weight": 6
      },
      "item-796": {
        "value": 6,
        "weight": 9
      },
      "item-797": {
        "value": 9,
        "weight": 3
      },
      "item-798": {
        "value": 6,
        "weight": 2
      },
      "item-799": {
        "value": 2,
        "weight": 8
      },
      "item-800": {
        "value": 3,
        "weight": 2
      },
      "item-801": {
        "value": 9,
        "weight": 6
      },
      "item-802": {
        "value": 3,
        "weight": 2
      },
      "item-803": {
        "value": 3,
        "weight": 6
      },
      "item-804": {
        "value": 1,
        "weight": 7
      },
      "item-805": {
        "value": 2,
        "weight": 4
      },
      "item-806": {
        "value": 9,
        "weight": 8
      },
      "item-807": {
        "value": 7,
        "weight": 7
      },
      "item-808": {
        "value": 3,
        "weight": 5
      },
      "item-809": {
        "value": 7,
        "weight": 8
      },
      "item-810": {
        "value": 6,
        "weight": 5
      },
      "item-811": {
        "value": 5,
        "weight": 3
      },
      "item-812": {
        "value": 7,
        "weight": 8
      },
      "item-813": {
        "value": 5,
        "weight": 1
      },
      "item-814": {
        "value": 9,
        "weight": 1
      },
      "item-815": {
        "value": 5,
        "weight": 7
      },
      "item-816": {
        "value": 2,
        "weight": 7
      },
      "item-817": {
        "value": 8,
        "weight": 3
      },
      "item-818": {
        "value": 7,
        "weight": 1
      },
      "item-819": {
        "value": 2,
        "weight": 6
      },
      "item-820": {
        "value": 7,
        "weight": 3
      },
      "item-821": {
        "value": 1,
        "weight": 6
      },
      "item-822": {
        "value": 9,
        "weight": 8
      },
      "item-823": {
        "value": 7,
        "weight": 4
      },
      "item-824": {
        "value": 7,
        "weight": 9
      },
      "item-825": {
        "value": 4,
        "weight": 1
      },
      "item-826": {
        "value": 5,
        "weight": 7
      },
      "item-827": {
        "value": 5,
        "weight": 3
      },
      "item-828": {
        "value": 1,
        "weight": 8
      },
      "item-829": {
        "value": 8,
        "weight": 9
      },
      "item-830": {
        "value": 2,
        "weight": 7
      },
      "item-831": {
        "value": 2,
        "weight": 9
      },
      "item-832": {
        "value": 3,
        "weight": 8
      },
      "item-833": {
        "value": 7,
        "weight": 9
      },
      "item-834": {
        "value": 8,
        "weight": 4
      },
      "item-835": {
        "value": 6,
        "weight": 3
      },
      "item-836": {
        "value": 4,
        "weight": 2
      },
      "item-837": {
        "value": 5,
        "weight": 7
      },
      "item-838": {
        "value": 4,
        "weight": 3
      },
      "item-839": {
        "value": 2,
        "weight": 4
      },
      "item-840": {
        "value": 4,
        "weight": 2
      },
      "item-841": {
        "value": 1,
        "weight": 9
      },
      "item-842": {
        "value": 2,
        "weight": 5
      },
      "item-843": {
        "value": 3,
        "weight": 5
      },
      "item-844": {
        "value": 1,
        "weight": 7
      },
      "item-845": {
        "value": 4,
        "weight": 5
      },
      "item-846": {
        "value": 3,
        "weight": 3
      },
      "item-847": {
        "value": 1,
        "weight": 1
      },
      "item-848": {
        "value": 9,
        "weight": 9
      },
      "item-849": {
        "value": 1,
        "weight": 5
      },
      "item-850": {
        "value": 4,
        "weight": 4
      },
      "item-851": {
        "value": 3,
        "weight": 7
      },
      "item-852": {
        "value": 2,
        "weight": 7
      },
      "item-853": {
        "value": 2,
        "weight": 2
      },
      "item-854": {
        "value": 2,
        "weight": 6
      },
      "item-855": {
        "value": 9,
        "weight": 9
      },
      "item-856": {
        "value": 7,
        "weight": 3
      },
      "item-857": {
        "value": 3,
        "weight": 9
      },
      "item-858": {
        "value": 9,
        "weight": 5
      },
      "item-859": {
        "value": 4,
        "weight": 3
      },
      "item-860": {
        "value": 3,
        "weight": 6
      },
      "item-861": {
        "value": 1,
        "weight": 1
      },
      "item-862": {
        "value": 2,
        "weight": 6
      },
      "item-863": {
        "value": 7,
        "weight": 2
      },
      "item-864": {
        "value": 7,
        "weight": 2
      },
      "item-865": {
        "value": 2,
        "weight": 2
      },
      "item-866": {
        "value": 8,
        "weight": 5
      },
      "item-867": {
        "value": 5,
        "weight": 9
      },
      "item-868": {
        "value": 7,
        "weight": 4
      },
      "item-869": {
        "value": 8,
        "weight": 6
      },
      "item-870": {
        "value": 4,
        "weight": 4
      },
      "item-871": {
        "value": 4,
        "weight": 6
      },
      "item-872": {
        "value": 7,
        "weight": 4
      },
      "item-873": {
        "value": 9,
        "weight": 8
      },
      "item-874": {
        "value": 6,
        "weight": 1
      },
      "item-875": {
        "value": 9,
        "weight": 5
      },
      "item-876": {
        "value": 4,
        "weight": 1
      },
      "item-877": {
        "value": 9,
        "weight": 1
      },
      "item-878": {
        "value": 1,
        "weight": 4
      },
      "item-879": {
        "value": 3,
        "weight": 7
      },
      "item-880": {
        "value": 8,
        "weight": 1
      },
      "item-881": {
        "value": 8,
        "weight": 9
      },
      "item-882": {
        "value": 9,
        "weight": 9
      },
      "item-883": {
        "value": 3,
        "weight": 4
      },
      "item-884": {
        "value": 2,
        "weight": 4
      },
      "item-885": {
        "value": 1,
        "weight": 9
      },
      "item-886": {
        "value": 2,
        "weight": 3
      },
      "item-887": {
        "value": 1,
        "weight": 5
      },
      "item-888": {
        "value": 7,
        "weight": 7
      },
      "item-889": {
        "value": 7,
        "weight": 4
      },
      "item-890": {
        "value": 3,
        "weight": 6
      },
      "item-891": {
        "value": 3,
        "weight": 7
      },
      "item-892": {
        "value": 5,
        "weight": 5
      },
      "item-893": {
        "value": 7,
        "weight": 5
      },
      "item-894": {
        "value": 1,
        "weight": 3
      },
      "item-895": {
        "value": 8,
        "weight": 7
      },
      "item-896": {
        "value": 4,
        "weight": 8
      },
      "item-897": {
        "value": 5,
        "weight": 8
      },
      "item-898": {
        "value": 3,
        "weight": 5
      },
      "item-899": {
        "value": 4,
        "weight": 2
      },
      "item-900": {
        "value": 2,
        "weight": 7
      },
      "item-901": {
        "value": 8,
        "weight": 7
      },
      "item-902": {
        "value": 6,
        "weight": 6
      },
      "item-903": {
        "value": 4,
        "weight": 5
      },
      "item-904": {
        "value": 5,
        "weight": 1
      },
      "item-905": {
        "value": 6,
        "weight": 1
      },
      "item-906": {
        "value": 8,
        "weight": 1
      },
      "item-907": {
        "value": 3,
        "weight": 7
      },
      "item-908": {
        "value": 2,
        "weight": 2
      },
      "item-909": {
        "value": 9,
        "weight": 5
      },
      "item-910": {
        "value": 6,
        "weight": 4
      },
      "item-911": {
        "value": 3,
        "weight": 7
      },
      "item-912": {
        "value": 3,
        "weight": 7
      },
      "item-913": {
        "value": 6,
        "weight": 7
      },
      "item-914": {
        "value": 7,
        "weight": 9
      },
      "item-915": {
        "value": 2,
        "weight": 7
      },
      "item-916": {
        "value": 6,
        "weight": 4
      },
      "item-917": {
        "value": 3,
        "weight": 8
      },
      "item-918": {
        "value": 4,
        "weight": 8
      },
      "item-919": {
        "value": 4,
        "weight": 5
      },
      "item-920": {
        "value": 6,
        "weight": 7
      },
      "item-921": {
        "value": 5,
        "weight": 1
      },
      "item-922": {
        "value": 5,
        "weight": 7
      },
      "item-923": {
        "value": 4,
        "weight": 9
      },
      "item-924": {
        "value": 4,
        "weight": 8
      },
      "item-925": {
        "value": 5,
        "weight": 7
      },
      "item-926": {
        "value": 1,
        "weight": 2
      },
      "item-927": {
        "value": 6,
        "weight": 7
      },
      "item-928": {
        "value": 1,
        "weight": 1
      },
      "item-929": {
        "value": 4,
        "weight": 2
      },
      "item-930": {
        "value": 5,
        "weight": 4
      },
      "item-931": {
        "value": 3,
        "weight": 5
      },
      "item-932": {
        "value": 6,
        "weight": 2
      },
      "item-933": {
        "value": 1,
        "weight": 8
      },
      "item-934": {
        "value": 2,
        "weight": 5
      },
      "item-935": {
        "value": 5,
        "weight": 5
      },
      "item-936": {
        "value": 7,
        "weight": 8
      },
      "item-937": {
        "value": 2,
        "weight": 9
      },
      "item-938": {
        "value": 5,
        "weight": 5
      },
      "item-939": {
        "value": 4,
        "weight": 9
      },
      "item-940": {
        "value": 6,
        "weight": 8
      },
      "item-941": {
        "value": 1,
        "weight": 3
      },
      "item-942": {
        "value": 2,
        "weight": 4
      },
      "item-943": {
        "value": 9,
        "weight": 4
      },
      "item-944": {
        "value": 1,
        "weight": 8
      },
      "item-945": {
        "value": 9,
        "weight": 1
      },
      "item-946": {
        "value": 1,
        "weight": 8
      },
      "item-947": {
        "value": 5,
        "weight": 6
      },
      "item-948": {
        "value": 7,
        "weight": 3
      },
      "item-949": {
        "value": 6,
        "weight": 2
      },
      "item-950": {
        "value": 6,
        "weight": 2
      },
      "item-951": {
        "value": 7,
        "weight": 8
      },
      "item-952": {
        "value": 2,
        "weight": 4
      },
      "item-953": {
        "value": 8,
        "weight": 9
      },
      "item-954": {
        "value": 8,
        "weight": 8
      },
      "item-955": {
        "value": 9,
        "weight": 1
      },
      "item-956": {
        "value": 3,
        "weight": 4
      },
      "item-957": {
        "value": 6,
        "weight": 6
      },
      "item-958": {
        "value": 2,
        "weight": 3
      },
      "item-959": {
        "value": 7,
        "weight": 7
      },
      "item-960": {
        "value": 2,
        "weight": 3
      },
      "item-961": {
        "value": 2,
        "weight": 4
      },
      "item-962": {
        "value": 7,
        "weight": 3
      },
      "item-963": {
        "value": 4,
        "weight": 1
      },
      "item-964": {
        "value": 3,
        "weight": 1
      },
      "item-965": {
        "value": 1,
        "weight": 6
      },
      "item-966": {
        "value": 5,
        "weight": 1
      },
      "item-967": {
        "value": 1,
        "weight": 4
      },
      "item-968": {
        "value": 7,
        "weight": 8
      },
      "item-969": {
        "value": 2,
        "weight": 2
      },
      "item-970": {
        "value": 3,
        "weight": 7
      },
      "item-971": {
        "value": 1,
        "weight": 5
      },
      "item-972": {
        "value": 8,
        "weight": 5
      },
      "item-973": {
        "value": 9,
        "weight": 1
      },
      "item-974": {
        "value": 9,
        "weight": 6
      },
      "item-975": {
        "value": 1,
        "weight": 2
      },
      "item-976": {
        "value": 7,
        "weight": 9
      },
      "item-977": {
        "value": 2,
        "weight": 1
      },
      "item-978": {
        "value": 4,
        "weight": 8
      },
      "item-979": {
        "value": 3,
        "weight": 6
      },
      "item-980": {
        "value": 8,
        "weight": 8
      },
      "item-981": {
        "value": 1,
        "weight": 8
      },
      "item-982": {
        "value": 8,
        "weight": 6
      },
      "item-983": {
        "value": 7,
        "weight": 8
      },
      "item-984": {
        "value": 1,
        "weight": 6
      },
      "item-985": {
        "value": 2,
        "weight": 5
      },
      "item-986": {
        "value": 3,
        "weight": 7
      },
      "item-987": {
        "value": 9,
        "weight": 5
      },
      "item-988": {
        "value": 3,
        "weight": 2
      },
      "item-989": {
        "value": 2,
        "weight": 9
      },
      "item-990": {
        "value": 7,
        "weight": 1
      },
      "item-991": {
        "value": 6,
        "weight": 1
      },
      "item-992": {
        "value": 4,
        "weight": 3
      },
      "item-993": {
        "value": 9,
        "weight": 9
      },
      "item-994": {
        "value": 8,
        "weight": 6
      },
      "item-995": {
        "value": 9,
        "weight": 2
      },
      "item-996": {
        "value": 8,
        "weight": 7
      },
      "item-997": {
        "value": 1,
        "weight": 2
      },
      "item-998": {
        "value": 9,
        "weight": 5
      },
      "item-999": {
        "value": 5,
        "weight": 2
      },
      "item-1000": {
        "value": 7,
        "weight": 8
      },
      "item-1001": {
        "value": 1,
        "weight": 1
      },
      "item-1002": {
        "value": 6,
        "weight": 6
      },
      "item-1003": {
        "value": 1,
        "weight": 4
      },
      "item-1004": {
        "value": 9,
        "weight": 4
      },
      "item-1005": {
        "value": 9,
        "weight": 3
      },
      "item-1006": {
        "value": 2,
        "weight": 9
      },
      "item-1007": {
        "value": 8,
        "weight": 1
      },
      "item-1008": {
        "value": 7,
        "weight": 8
      },
      "item-1009": {
        "value": 3,
        "weight": 9
      },
      "item-1010": {
        "value": 2,
        "weight": 5
      },
      "item-1011": {
        "value": 3,
        "weight": 1
      },
      "item-1012": {
        "value": 7,
        "weight": 1
      },
      "item-1013": {
        "value": 5,
        "weight": 2
      },
      "item-1014": {
        "value": 3,
        "weight": 5
      },
      "item-1015": {
        "value": 1,
        "weight": 3
      },
      "item-1016": {
        "value": 2,
        "weight": 6
      },
      "item-1017": {
        "value": 1,
        "weight": 6
      },
      "item-1018": {
        "value": 8,
        "weight": 9
      },
      "item-1019": {
        "value": 7,
        "weight": 5
      },
      "item-1020": {
        "value": 8,
        "weight": 8
      },
      "item-1021": {
        "value": 9,
        "weight": 9
      },
      "item-1022": {
        "value": 1,
        "weight": 7
      },
      "item-1023": {
        "value": 7,
        "weight": 3
      },
      "item-1024": {
        "value": 7,
        "weight": 1
      },
      "item-1025": {
        "value": 6,
        "weight": 2
      },
      "item-1026": {
        "value": 4,
        "weight": 4
      },
      "item-1027": {
        "value": 9,
        "weight": 8
      },
      "item-1028": {
        "value": 7,
        "weight": 2
      },
      "item-1029": {
        "value": 2,
        "weight": 6
      },
      "item-1030": {
        "value": 5,
        "weight": 1
      },
      "item-1031": {
        "value": 5,
        "weight": 1
      },
      "item-1032": {
        "value": 9,
        "weight": 8
      },
      "item-1033": {
        "value": 4,
        "weight": 8
      },
      "item-1034": {
        "value": 8,
        "weight": 7
      },
      "item-1035": {
        "value": 1,
        "weight": 6
      },
      "item-1036": {
        "value": 7,
        "weight": 7
      },
      "item-1037": {
        "value": 4,
        "weight": 1
      },
      "item-1038": {
        "value": 1,
        "weight": 3
      },
      "item-1039": {
        "value": 3,
        "weight": 5
      },
      "item-1040": {
        "value": 2,
        "weight": 4
      },
      "item-1041": {
        "value": 3,
        "weight": 8
      },
      "item-1042": {
        "value": 2,
        "weight": 9
      },
      "item-1043": {
        "value": 8,
        "weight": 9
      },
      "item-1044": {
        "value": 9,
        "weight": 6
      },
      "item-1045": {
        "value": 8,
        "weight": 8
      },
      "item-1046": {
        "value": 9,
        "weight": 9
      },
      "item-1047": {
        "value": 7,
        "weight": 8
      },
      "item-1048": {
        "value": 9,
        "weight": 2
      },
      "item-1049": {
        "value": 7,
        "weight": 9
      },
      "item-1050": {
        "value": 4,
        "weight": 6
      },
      "item-1051": {
        "value": 1,
        "weight": 6
      },
      "item-1052": {
        "value": 9,
        "weight": 6
      },
      "item-1053": {
        "value": 9,
        "weight": 3
      },
      "item-1054": {
        "value": 6,
        "weight": 1
      },
      "item-1055": {
        "value": 5,
        "weight": 7
      },
      "item-1056": {
        "value": 9,
        "weight": 4
      },
      "item-1057": {
        "value": 1,
        "weight": 6
      },
      "item-1058": {
        "value": 8,
        "weight": 7
      },
      "item-1059": {
        "value": 5,
        "weight": 4
      },
      "item-1060": {
        "value": 6,
        "weight": 7
      },
      "item-1061": {
        "value": 1,
        "weight": 1
      },
      "item-1062": {
        "value": 4,
        "weight": 9
      },
      "item-1063": {
        "value": 2,
        "weight": 1
      },
      "item-1064": {
        "value": 4,
        "weight": 2
      },
      "item-1065": {
        "value": 3,
        "weight": 2
      },
      "item-1066": {
        "value": 7,
        "weight": 7
      },
      "item-1067": {
        "value": 8,
        "weight": 9
      },
      "item-1068": {
        "value": 2,
        "weight": 5
      },
      "item-1069": {
        "value": 7,
        "weight": 2
      },
      "item-1070": {
        "value": 9,
        "weight": 2
      },
      "item-1071": {
        "value": 4,
        "weight": 6
      },
      "item-1072": {
        "value": 4,
        "weight": 7
      },
      "item-1073": {
        "value": 7,
        "weight": 5
      },
      "item-1074": {
        "value": 9,
        "weight": 7
      },
      "item-1075": {
        "value": 5,
        "weight": 2
      },
      "item-1076": {
        "value": 3,
        "weight": 5
      },
      "item-1077": {
        "value": 8,
        "weight": 3
      },
      "item-1078": {
        "value": 5,
        "weight": 9
      },
      "item-1079": {
        "value": 4,
        "weight": 3
      },
      "item-1080": {
        "value": 3,
        "weight": 9
      },
      "item-1081": {
        "value": 1,
        "weight": 5
      },
      "item-1082": {
        "value": 8,
        "weight": 8
      },
      "item-1083": {
        "value": 6,
        "weight": 8
      },
      "item-1084": {
        "value": 5,
        "weight": 8
      },
      "item-1085": {
        "value": 7,
        "weight": 1
      },
      "item-1086": {
        "value": 7,
        "weight": 5
      },
      "item-1087": {
        "value": 8,
        "weight": 3
      },
      "item-1088": {
        "value": 1,
        "weight": 4
      },
      "item-1089": {
        "value": 7,
        "weight": 8
      },
      "item-1090": {
        "value": 2,
        "weight": 6
      },
      "item-1091": {
        "value": 9,
        "weight": 8
      },
      "item-1092": {
        "value": 5,
        "weight": 2
      },
      "item-1093": {
        "value": 4,
        "weight": 3
      },
      "item-1094": {
        "value": 7,
        "weight": 4
      },
      "item-1095": {
        "value": 1,
        "weight": 6
      },
      "item-1096": {
        "value": 5,
        "weight": 1
      },
      "item-1097": {
        "value": 4,
        "weight": 3
      },
      "item-1098": {
        "value": 5,
        "weight": 4
      },
      "item-1099": {
        "value": 7,
        "weight": 8
      },
      "item-1100": {
        "value": 1,
        "weight": 7
      },
      "item-1101": {
        "value": 9,
        "weight": 9
      },
      "item-1102": {
        "value": 9,
        "weight": 3
      },
      "item-1103": {
        "value": 4,
        "weight": 2
      },
      "item-1104": {
        "value": 9,
        "weight": 6
      },
      "item-1105": {
        "value": 6,
        "weight": 8
      },
      "item-1106": {
        "value": 8,
        "weight": 8
      },
      "item-1107": {
        "value": 8,
        "weight": 8
      },
      "item-1108": {
        "value": 9,
        "weight": 8
      },
      "item-1109": {
        "value": 8,
        "weight": 6
      },
      "item-1110": {
        "value": 7,
        "weight": 9
      },
      "item-1111": {
        "value": 4,
        "weight": 8
      },
      "item-1112": {
        "value": 4,
        "weight": 9
      },
      "item-1113": {
        "value": 9,
        "weight": 8
      },
      "item-1114": {
        "value": 1,
        "weight": 5
      },
      "item-1115": {
        "value": 3,
        "weight": 4
      },
      "item-1116": {
        "value": 1,
        "weight": 5
      },
      "item-1117": {
        "value": 9,
        "weight": 7
      },
      "item-1118": {
        "value": 3,
        "weight": 6
      },
      "item-1119": {
        "value": 3,
        "weight": 4
      },
      "item-1120": {
        "value": 7,
        "weight": 5
      },
      "item-1121": {
        "value": 4,
        "weight": 2
      },
      "item-1122": {
        "value": 3,
        "weight": 1
      },
      "item-1123": {
        "value": 1,
        "weight": 9
      },
      "item-1124": {
        "value": 2,
        "weight": 8
      },
      "item-1125": {
        "value": 1,
        "weight": 1
      },
      "item-1126": {
        "value": 1,
        "weight": 3
      },
      "item-1127": {
        "value": 7,
        "weight": 3
      },
      "item-1128": {
        "value": 7,
        "weight": 4
      },
      "item-1129": {
        "value": 8,
        "weight": 5
      },
      "item-1130": {
        "value": 4,
        "weight": 7
      },
      "item-1131": {
        "value": 7,
        "weight": 1
      },
      "item-1132": {
        "value": 6,
        "weight": 3
      },
      "item-1133": {
        "value": 1,
        "weight": 5
      },
      "item-1134": {
        "value": 7,
        "weight": 1
      },
      "item-1135": {
        "value": 8,
        "weight": 5
      },
      "item-1136": {
        "value": 5,
        "weight": 3
      },
      "item-1137": {
        "value": 9,
        "weight": 5
      },
      "item-1138": {
        "value": 6,
        "weight": 9
      },
      "item-1139": {
        "value": 1,
        "weight": 9
      },
      "item-1140": {
        "value": 6,
        "weight": 5
      },
      "item-1141": {
        "value": 5,
        "weight": 8
      },
      "item-1142": {
        "value": 2,
        "weight": 9
      },
      "item-1143": {
        "value": 5,
        "weight": 8
      },
      "item-1144": {
        "value": 8,
        "weight": 3
      },
      "item-1145": {
        "value": 9,
        "weight": 7
      },
      "item-1146": {
        "value": 8,
        "weight": 7
      },
      "item-1147": {
        "value": 4,
        "weight": 9
      },
      "item-1148": {
        "value": 8,
        "weight": 4
      },
      "item-1149": {
        "value": 4,
        "weight": 2
      },
      "item-1150": {
        "value": 3,
        "weight": 4
      },
      "item-1151": {
        "value": 7,
        "weight": 7
      },
      "item-1152": {
        "value": 6,
        "weight": 5
      },
      "item-1153": {
        "value": 7,
        "weight": 5
      },
      "item-1154": {
        "value": 3,
        "weight": 3
      },
      "item-1155": {
        "value": 6,
        "weight": 9
      },
      "item-1156": {
        "value": 5,
        "weight": 9
      },
      "item-1157": {
        "value": 2,
        "weight": 1
      },
      "item-1158": {
        "value": 8,
        "weight": 7
      },
      "item-1159": {
        "value": 2,
        "weight": 7
      },
      "item-1160": {
        "value": 3,
        "weight": 1
      },
      "item-1161": {
        "value": 7,
        "weight": 7
      },
      "item-1162": {
        "value": 3,
        "weight": 4
      },
      "item-1163": {
        "value": 4,
        "weight": 5
      },
      "item-1164": {
        "value": 1,
        "weight": 9
      },
      "item-1165": {
        "value": 5,
        "weight": 9
      },
      "item-1166": {
        "value": 3,
        "weight": 2
      },
      "item-1167": {
        "value": 7,
        "weight": 7
      },
      "item-1168": {
        "value": 8,
        "weight": 7
      },
      "item-1169": {
        "value": 2,
        "weight": 8
      },
      "item-1170": {
        "value": 4,
        "weight": 6
      },
      "item-1171": {
        "value": 2,
        "weight": 5
      },
      "item-1172": {
        "value": 9,
        "weight": 8
      },
      "item-1173": {
        "value": 8,
        "weight": 9
      },
      "item-1174": {
        "value": 7,
        "weight": 9
      },
      "item-1175": {
        "value": 1,
        "weight": 2
      },
      "item-1176": {
        "value": 4,
        "weight": 4
      },
      "item-1177": {
        "value": 1,
        "weight": 5
      },
      "item-1178": {
        "value": 1,
        "weight": 2
      },
      "item-1179": {
        "value": 2,
        "weight": 5
      },
      "item-1180": {
        "value": 6,
        "weight": 1
      },
      "item-1181": {
        "value": 1,
        "weight": 1
      },
      "item-1182": {
        "value": 2,
        "weight": 5
      },
      "item-1183": {
        "value": 4,
        "weight": 6
      },
      "item-1184": {
        "value": 6,
        "weight": 9
      },
      "item-1185": {
        "value": 4,
        "weight": 2
      },
      "item-1186": {
        "value": 1,
        "weight": 2
      },
      "item-1187": {
        "value": 4,
        "weight": 1
      },
      "item-1188": {
        "value": 3,
        "weight": 2
      },
      "item-1189": {
        "value": 3,
        "weight": 7
      },
      "item-1190": {
        "value": 9,
        "weight": 9
      },
      "item-1191": {
        "value": 5,
        "weight": 4
      },
      "item-1192": {
        "value": 8,
        "weight": 7
      },
      "item-1193": {
        "value": 7,
        "weight": 4
      },
      "item-1194": {
        "value": 9,
        "weight": 5
      },
      "item-1195": {
        "value": 3,
        "weight": 6
      },
      "item-1196": {
        "value": 4,
        "weight": 7
      },
      "item-1197": {
        "value": 9,
        "weight": 1
      },
      "item-1198": {
        "value": 2,
        "weight": 6
      },
      "item-1199": {
        "value": 3,
        "weight": 8
      },
      "item-1200": {
        "value": 3,
        "weight": 6
      },
      "item-1201": {
        "value": 2,
        "weight": 2
      },
      "item-1202": {
        "value": 3,
        "weight": 1
      },
      "item-1203": {
        "value": 8,
        "weight": 3
      },
      "item-1204": {
        "value": 4,
        "weight": 8
      },
      "item-1205": {
        "value": 4,
        "weight": 9
      },
      "item-1206": {
        "value": 7,
        "weight": 2
      },
      "item-1207": {
        "value": 1,
        "weight": 9
      },
      "item-1208": {
        "value": 7,
        "weight": 3
      },
      "item-1209": {
        "value": 6,
        "weight": 6
      },
      "item-1210": {
        "value": 9,
        "weight": 6
      },
      "item-1211": {
        "value": 8,
        "weight": 2
      },
      "item-1212": {
        "value": 5,
        "weight": 3
      },
      "item-1213": {
        "value": 5,
        "weight": 2
      },
      "item-1214": {
        "value": 1,
        "weight": 6
      },
      "item-1215": {
        "value": 9,
        "weight": 7
      },
      "item-1216": {
        "value": 1,
        "weight": 5
      },
      "item-1217": {
        "value": 6,
        "weight": 4
      },
      "item-1218": {
        "value": 1,
        "weight": 9
      },
      "item-1219": {
        "value": 8,
        "weight": 4
      },
      "item-1220": {
        "value": 5,
        "weight": 8
      },
      "item-1221": {
        "value": 6,
        "weight": 9
      },
      "item-1222": {
        "value": 9,
        "weight": 9
      },
      "item-1223": {
        "value": 8,
        "weight": 5
      },
      "item-1224": {
        "value": 3,
        "weight": 4
      },
      "item-1225": {
        "value": 9,
        "weight": 2
      },
      "item-1226": {
        "value": 4,
        "weight": 5
      },
      "item-1227": {
        "value": 5,
        "weight": 4
      },
      "item-1228": {
        "value": 9,
        "weight": 9
      },
      "item-1229": {
        "value": 3,
        "weight": 1
      },
      "item-1230": {
        "value": 5,
        "weight": 6
      },
      "item-1231": {
        "value": 5,
        "weight": 8
      },
      "item-1232": {
        "value": 9,
        "weight": 3
      },
      "item-1233": {
        "value": 6,
        "weight": 8
      },
      "item-1234": {
        "value": 5,
        "weight": 1
      },
      "item-1235": {
        "value": 6,
        "weight": 1
      },
      "item-1236": {
        "value": 5,
        "weight": 7
      },
      "item-1237": {
        "value": 6,
        "weight": 3
      },
      "item-1238": {
        "value": 8,
        "weight": 4
      },
      "item-1239": {
        "value": 4,
        "weight": 1
      },
      "item-1240": {
        "value": 6,
        "weight": 1
      },
      "item-1241": {
        "value": 1,
        "weight": 2
      },
      "item-1242": {
        "value": 3,
        "weight": 8
      },
      "item-1243": {
        "value": 2,
        "weight": 1
      },
      "item-1244": {
        "value": 8,
        "weight": 8
      },
      "item-1245": {
        "value": 3,
        "weight": 4
      },
      "item-1246": {
        "value": 2,
        "weight": 7
      },
      "item-1247": {
        "value": 4,
        "weight": 7
      },
      "item-1248": {
        "value": 7,
        "weight": 3
      },
      "item-1249": {
        "value": 7,
        "weight": 2
      },
      "item-1250": {
        "value": 8,
        "weight": 6
      },
      "item-1251": {
        "value": 4,
        "weight": 7
      },
      "item-1252": {
        "value": 3,
        "weight": 1
      },
      "item-1253": {
        "value": 1,
        "weight": 3
      },
      "item-1254": {
        "value": 1,
        "weight": 6
      },
      "item-1255": {
        "value": 9,
        "weight": 6
      },
      "item-1256": {
        "value": 3,
        "weight": 8
      },
      "item-1257": {
        "value": 8,
        "weight": 4
      },
      "item-1258": {
        "value": 9,
        "weight": 9
      },
      "item-1259": {
        "value": 4,
        "weight": 4
      },
      "item-1260": {
        "value": 5,
        "weight": 6
      },
      "item-1261": {
        "value": 2,
        "weight": 5
      },
      "item-1262": {
        "value": 7,
        "weight": 4
      },
      "item-1263": {
        "value": 3,
        "weight": 6
      },
      "item-1264": {
        "value": 2,
        "weight": 3
      },
      "item-1265": {
        "value": 7,
        "weight": 9
      },
      "item-1266": {
        "value": 4,
        "weight": 8
      },
      "item-1267": {
        "value": 5,
        "weight": 9
      },
      "item-1268": {
        "value": 9,
        "weight": 6
      },
      "item-1269": {
        "value": 2,
        "weight": 1
      },
      "item-1270": {
        "value": 2,
        "weight": 9
      },
      "item-1271": {
        "value": 7,
        "weight": 6
      },
      "item-1272": {
        "value": 3,
        "weight": 5
      },
      "item-1273": {
        "value": 7,
        "weight": 6
      },
      "item-1274": {
        "value": 9,
        "weight": 3
      },
      "item-1275": {
        "value": 1,
        "weight": 3
      },
      "item-1276": {
        "value": 5,
        "weight": 5
      },
      "item-1277": {
        "value": 5,
        "weight": 2
      },
      "item-1278": {
        "value": 2,
        "weight": 4
      },
      "item-1279": {
        "value": 2,
        "weight": 4
      },
      "item-1280": {
        "value": 4,
        "weight": 9
      },
      "item-1281": {
        "value": 4,
        "weight": 6
      },
      "item-1282": {
        "value": 9,
        "weight": 1
      },
      "item-1283": {
        "value": 7,
        "weight": 2
      },
      "item-1284": {
        "value": 7,
        "weight": 2
      },
      "item-1285": {
        "value": 6,
        "weight": 9
      },
      "item-1286": {
        "value": 3,
        "weight": 8
      },
      "item-1287": {
        "value": 5,
        "weight": 3
      },
      "item-1288": {
        "value": 5,
        "weight": 5
      },
      "item-1289": {
        "value": 5,
        "weight": 7
      },
      "item-1290": {
        "value": 4,
        "weight": 6
      },
      "item-1291": {
        "value": 8,
        "weight": 7
      },
      "item-1292": {
        "value": 7,
        "weight": 8
      },
      "item-1293": {
        "value": 1,
        "weight": 3
      },
      "item-1294": {
        "value": 3,
        "weight": 1
      },
      "item-1295": {
        "value": 2,
        "weight": 6
      },
      "item-1296": {
        "value": 1,
        "weight": 8
      },
      "item-1297": {
        "value": 9,
        "weight": 8
      },
      "item-1298": {
        "value": 9,
        "weight": 1
      },
      "item-1299": {
        "value": 4,
        "weight": 5
      },
      "item-1300": {
        "value": 8,
        "weight": 8
      },
      "item-1301": {
        "value": 5,
        "weight": 3
      },
      "item-1302": {
        "value": 1,
        "weight": 7
      },
      "item-1303": {
        "value": 2,
        "weight": 7
      },
      "item-1304": {
        "value": 6,
        "weight": 6
      },
      "item-1305": {
        "value": 9,
        "weight": 9
      },
      "item-1306": {
        "value": 4,
        "weight": 2
      },
      "item-1307": {
        "value": 9,
        "weight": 4
      },
      "item-1308": {
        "value": 9,
        "weight": 3
      },
      "item-1309": {
        "value": 8,
        "weight": 8
      },
      "item-1310": {
        "value": 6,
        "weight": 1
      },
      "item-1311": {
        "value": 1,
        "weight": 6
      },
      "item-1312": {
        "value": 3,
        "weight": 1
      },
      "item-1313": {
        "value": 6,
        "weight": 4
      },
      "item-1314": {
        "value": 4,
        "weight": 4
      },
      "item-1315": {
        "value": 1,
        "weight": 9
      },
      "item-1316": {
        "value": 9,
        "weight": 7
      },
      "item-1317": {
        "value": 5,
        "weight": 8
      },
      "item-1318": {
        "value": 4,
        "weight": 2
      },
      "item-1319": {
        "value": 4,
        "weight": 7
      },
      "item-1320": {
        "value": 4,
        "weight": 6
      },
      "item-1321": {
        "value": 1,
        "weight": 1
      },
      "item-1322": {
        "value": 1,
        "weight": 5
      },
      "item-1323": {
        "value": 1,
        "weight": 6
      },
      "item-1324": {
        "value": 7,
        "weight": 2
      },
      "item-1325": {
        "value": 7,
        "weight": 5
      },
      "item-1326": {
        "value": 2,
        "weight": 9
      },
      "item-1327": {
        "value": 6,
        "weight": 3
      },
      "item-1328": {
        "value": 9,
        "weight": 7
      },
      "item-1329": {
        "value": 9,
        "weight": 6
      },
      "item-1330": {
        "value": 2,
        "weight": 3
      },
      "item-1331": {
        "value": 3,
        "weight": 6
      },
      "item-1332": {
        "value": 9,
        "weight": 6
      },
      "item-1333": {
        "value": 3,
        "weight": 5
      },
      "item-1334": {
        "value": 5,
        "weight": 1
      },
      "item-1335": {
        "value": 5,
        "weight": 6
      },
      "item-1336": {
        "value": 9,
        "weight": 4
      },
      "item-1337": {
        "value": 6,
        "weight": 6
      },
      "item-1338": {
        "value": 8,
        "weight": 8
      },
      "item-1339": {
        "value": 2,
        "weight": 1
      },
      "item-1340": {
        "value": 8,
        "weight": 9
      },
      "item-1341": {
        "value": 6,
        "weight": 1
      },
      "item-1342": {
        "value": 5,
        "weight": 9
      },
      "item-1343": {
        "value": 1,
        "weight": 3
      },
      "item-1344": {
        "value": 6,
        "weight": 1
      },
      "item-1345": {
        "value": 5,
        "weight": 5
      },
      "item-1346": {
        "value": 4,
        "weight": 8
      },
      "item-1347": {
        "value": 1,
        "weight": 1
      },
      "item-1348": {
        "value": 5,
        "weight": 5
      },
      "item-1349": {
        "value": 8,
        "weight": 7
      },
      "item-1350": {
        "value": 7,
        "weight": 7
      },
      "item-1351": {
        "value": 5,
        "weight": 9
      },
      "item-1352": {
        "value": 5,
        "weight": 4
      },
      "item-1353": {
        "value": 8,
        "weight": 2
      },
      "item-1354": {
        "value": 5,
        "weight": 1
      },
      "item-1355": {
        "value": 3,
        "weight": 6
      },
      "item-1356": {
        "value": 8,
        "weight": 3
      },
      "item-1357": {
        "value": 8,
        "weight": 6
      },
      "item-1358": {
        "value": 8,
        "weight": 9
      },
      "item-1359": {
        "value": 2,
        "weight": 2
      },
      "item-1360": {
        "value": 8,
        "weight": 1
      },
      "item-1361": {
        "value": 6,
        "weight": 5
      },
      "item-1362": {
        "value": 9,
        "weight": 3
      },
      "item-1363": {
        "value": 9,
        "weight": 6
      },
      "item-1364": {
        "value": 7,
        "weight": 8
      },
      "item-1365": {
        "value": 7,
        "weight": 7
      },
      "item-1366": {
        "value": 2,
        "weight": 4
      },
      "item-1367": {
        "value": 7,
        "weight": 3
      },
      "item-1368": {
        "value": 2,
        "weight": 5
      },
      "item-1369": {
        "value": 7,
        "weight": 3
      },
      "item-1370": {
        "value": 4,
        "weight": 5
      },
      "item-1371": {
        "value": 6,
        "weight": 8
      },
      "item-1372": {
        "value": 2,
        "weight": 7
      },
      "item-1373": {
        "value": 3,
        "weight": 7
      },
      "item-1374": {
        "value": 1,
        "weight": 6
      },
      "item-1375": {
        "value": 9,
        "weight": 8
      },
      "item-1376": {
        "value": 5,
        "weight": 2
      },
      "item-1377": {
        "value": 4,
        "weight": 4
      },
      "item-1378": {
        "value": 2,
        "weight": 6
      },
      "item-1379": {
        "value": 9,
        "weight": 8
      },
      "item-1380": {
        "value": 5,
        "weight": 1
      },
      "item-1381": {
        "value": 6,
        "weight": 3
      },
      "item-1382": {
        "value": 9,
        "weight": 3
      },
      "item-1383": {
        "value": 6,
        "weight": 1
      },
      "item-1384": {
        "value": 7,
        "weight": 2
      },
      "item-1385": {
        "value": 9,
        "weight": 5
      },
      "item-1386": {
        "value": 3,
        "weight": 6
      },
      "item-1387": {
        "value": 7,
        "weight": 7
      },
      "item-1388": {
        "value": 2,
        "weight": 3
      },
      "item-1389": {
        "value": 9,
        "weight": 4
      },
      "item-1390": {
        "value": 7,
        "weight": 6
      },
      "item-1391": {
        "value": 7,
        "weight": 3
      },
      "item-1392": {
        "value": 4,
        "weight": 6
      },
      "item-1393": {
        "value": 1,
        "weight": 8
      },
      "item-1394": {
        "value": 8,
        "weight": 4
      },
      "item-1395": {
        "value": 2,
        "weight": 7
      },
      "item-1396": {
        "value": 2,
        "weight": 9
      },
      "item-1397": {
        "value": 3,
        "weight": 6
      },
      "item-1398": {
        "value": 3,
        "weight": 2
      },
      "item-1399": {
        "value": 9,
        "weight": 3
      },
      "item-1400": {
        "value": 1,
        "weight": 2
      },
      "item-1401": {
        "value": 9,
        "weight": 9
      },
      "item-1402": {
        "value": 1,
        "weight": 7
      },
      "item-1403": {
        "value": 7,
        "weight": 5
      },
      "item-1404": {
        "value": 7,
        "weight": 8
      },
      "item-1405": {
        "value": 7,
        "weight": 8
      },
      "item-1406": {
        "value": 4,
        "weight": 5
      },
      "item-1407": {
        "value": 5,
        "weight": 5
      },
      "item-1408": {
        "value": 6,
        "weight": 8
      },
      "item-1409": {
        "value": 2,
        "weight": 8
      },
      "item-1410": {
        "value": 3,
        "weight": 2
      },
      "item-1411": {
        "value": 3,
        "weight": 8
      },
      "item-1412": {
        "value": 6,
        "weight": 9
      },
      "item-1413": {
        "value": 5,
        "weight": 8
      },
      "item-1414": {
        "value": 8,
        "weight": 6
      },
      "item-1415": {
        "value": 8,
        "weight": 4
      },
      "item-1416": {
        "value": 4,
        "weight": 9
      },
      "item-1417": {
        "value": 3,
        "weight": 6
      },
      "item-1418": {
        "value": 2,
        "weight": 3
      },
      "item-1419": {
        "value": 7,
        "weight": 5
      },
      "item-1420": {
        "value": 6,
        "weight": 7
      },
      "item-1421": {
        "value": 7,
        "weight": 4
      },
      "item-1422": {
        "value": 1,
        "weight": 5
      },
      "item-1423": {
        "value": 7,
        "weight": 2
      },
      "item-1424": {
        "value": 2,
        "weight": 4
      },
      "item-1425": {
        "value": 8,
        "weight": 3
      },
      "item-1426": {
        "value": 2,
        "weight": 6
      },
      "item-1427": {
        "value": 3,
        "weight": 1
      },
      "item-1428": {
        "value": 4,
        "weight": 6
      },
      "item-1429": {
        "value": 3,
        "weight": 4
      },
      "item-1430": {
        "value": 9,
        "weight": 9
      },
      "item-1431": {
        "value": 8,
        "weight": 6
      },
      "item-1432": {
        "value": 2,
        "weight": 3
      },
      "item-1433": {
        "value": 5,
        "weight": 1
      },
      "item-1434": {
        "value": 9,
        "weight": 2
      },
      "item-1435": {
        "value": 9,
        "weight": 5
      },
      "item-1436": {
        "value": 6,
        "weight": 4
      },
      "item-1437": {
        "value": 5,
        "weight": 7
      },
      "item-1438": {
        "value": 6,
        "weight": 3
      },
      "item-1439": {
        "value": 5,
        "weight": 9
      },
      "item-1440": {
        "value": 9,
        "weight": 5
      },
      "item-1441": {
        "value": 2,
        "weight": 3
      },
      "item-1442": {
        "value": 7,
        "weight": 3
      },
      "item-1443": {
        "value": 6,
        "weight": 1
      },
      "item-1444": {
        "value": 4,
        "weight": 5
      },
      "item-1445": {
        "value": 2,
        "weight": 6
      },
      "item-1446": {
        "value": 7,
        "weight": 8
      },
      "item-1447": {
        "value": 7,
        "weight": 3
      },
      "item-1448": {
        "value": 3,
        "weight": 8
      },
      "item-1449": {
        "value": 7,
        "weight": 7
      },
      "item-1450": {
        "value": 7,
        "weight": 4
      },
      "item-1451": {
        "value": 7,
        "weight": 4
      },
      "item-1452": {
        "value": 5,
        "weight": 4
      },
      "item-1453": {
        "value": 6,
        "weight": 9
      },
      "item-1454": {
        "value": 1,
        "weight": 3
      },
      "item-1455": {
        "value": 8,
        "weight": 7
      },
      "item-1456": {
        "value": 2,
        "weight": 4
      },
      "item-1457": {
        "value": 5,
        "weight": 5
      },
      "item-1458": {
        "value": 3,
        "weight": 1
      },
      "item-1459": {
        "value": 9,
        "weight": 9
      },
      "item-1460": {
        "value": 5,
        "weight": 6
      },
      "item-1461": {
        "value": 7,
        "weight": 4
      },
      "item-1462": {
        "value": 4,
        "weight": 3
      },
      "item-1463": {
        "value": 6,
        "weight": 9
      },
      "item-1464": {
        "value": 5,
        "weight": 6
      },
      "item-1465": {
        "value": 1,
        "weight": 2
      },
      "item-1466": {
        "value": 5,
        "weight": 6
      },
      "item-1467": {
        "value": 1,
        "weight": 5
      },
      "item-1468": {
        "value": 2,
        "weight": 6
      },
      "item-1469": {
        "value": 9,
        "weight": 1
      },
      "item-1470": {
        "value": 2,
        "weight": 4
      },
      "item-1471": {
        "value": 8,
        "weight": 2
      },
      "item-1472": {
        "value": 4,
        "weight": 3
      },
      "item-1473": {
        "value": 7,
        "weight": 9
      },
      "item-1474": {
        "value": 9,
        "weight": 7
      },
      "item-1475": {
        "value": 8,
        "weight": 1
      },
      "item-1476": {
        "value": 7,
        "weight": 8
      },
      "item-1477": {
        "value": 9,
        "weight": 4
      },
      "item-1478": {
        "value": 9,
        "weight": 3
      },
      "item-1479": {
        "value": 7,
        "weight": 8
      },
      "item-1480": {
        "value": 3,
        "weight": 3
      },
      "item-1481": {
        "value": 6,
        "weight": 2
      },
      "item-1482": {
        "value": 1,
        "weight": 6
      },
      "item-1483": {
        "value": 1,
        "weight": 7
      },
      "item-1484": {
        "value": 7,
        "weight": 3
      },
      "item-1485": {
        "value": 7,
        "weight": 3
      },
      "item-1486": {
        "value": 2,
        "weight": 3
      },
      "item-1487": {
        "value": 8,
        "weight": 6
      },
      "item-1488": {
        "value": 6,
        "weight": 7
      },
      "item-1489": {
        "value": 7,
        "weight": 2
      },
      "item-1490": {
        "value": 9,
        "weight": 2
      },
      "item-1491": {
        "value": 8,
        "weight": 4
      },
      "item-1492": {
        "value": 8,
        "weight": 1
      },
      "item-1493": {
        "value": 4,
        "weight": 5
      },
      "item-1494": {
        "value": 1,
        "weight": 3
      },
      "item-1495": {
        "value": 2,
        "weight": 8
      },
      "item-1496": {
        "value": 3,
        "weight": 1
      },
      "item-1497": {
        "value": 6,
        "weight": 6
      },
      "item-1498": {
        "value": 4,
        "weight": 2
      },
      "item-1499": {
        "value": 5,
        "weight": 1
      },
      "item-1500": {
        "value": 3,
        "weight": 1
      },
      "item-1501": {
        "value": 3,
        "weight": 3
      },
      "item-1502": {
        "value": 7,
        "weight": 4
      },
      "item-1503": {
        "value": 9,
        "weight": 3
      },
      "item-1504": {
        "value": 6,
        "weight": 2
      },
      "item-1505": {
        "value": 6,
        "weight": 8
      },
      "item-1506": {
        "value": 6,
        "weight": 7
      },
      "item-1507": {
        "value": 3,
        "weight": 2
      },
      "item-1508": {
        "value": 7,
        "weight": 1
      },
      "item-1509": {
        "value": 4,
        "weight": 9
      },
      "item-1510": {
        "value": 1,
        "weight": 2
      },
      "item-1511": {
        "value": 2,
        "weight": 3
      },
      "item-1512": {
        "value": 5,
        "weight": 1
      },
      "item-1513": {
        "value": 6,
        "weight": 5
      },
      "item-1514": {
        "value": 8,
        "weight": 7
      },
      "item-1515": {
        "value": 5,
        "weight": 6
      },
      "item-1516": {
        "value": 1,
        "weight": 7
      },
      "item-1517": {
        "value": 7,
        "weight": 1
      },
      "item-1518": {
        "value": 1,
        "weight": 2
      },
      "item-1519": {
        "value": 3,
        "weight": 4
      },
      "item-1520": {
        "value": 2,
        "weight": 4
      },
      "item-1521": {
        "value": 1,
        "weight": 7
      },
      "item-1522": {
        "value": 4,
        "weight": 7
      },
      "item-1523": {
        "value": 2,
        "weight": 7
      },
      "item-1524": {
        "value": 7,
        "weight": 2
      },
      "item-1525": {
        "value": 8,
        "weight": 2
      },
      "item-1526": {
        "value": 1,
        "weight": 2
      },
      "item-1527": {
        "value": 1,
        "weight": 2
      },
      "item-1528": {
        "value": 9,
        "weight": 1
      },
      "item-1529": {
        "value": 6,
        "weight": 3
      },
      "item-1530": {
        "value": 1,
        "weight": 7
      },
      "item-1531": {
        "value": 5,
        "weight": 8
      },
      "item-1532": {
        "value": 8,
        "weight": 1
      },
      "item-1533": {
        "value": 7,
        "weight": 8
      },
      "item-1534": {
        "value": 4,
        "weight": 9
      },
      "item-1535": {
        "value": 6,
        "weight": 3
      },
      "item-1536": {
        "value": 7,
        "weight": 3
      },
      "item-1537": {
        "value": 1,
        "weight": 9
      },
      "item-1538": {
        "value": 9,
        "weight": 3
      },
      "item-1539": {
        "value": 4,
        "weight": 3
      },
      "item-1540": {
        "value": 6,
        "weight": 6
      },
      "item-1541": {
        "value": 8,
        "weight": 8
      },
      "item-1542": {
        "value": 7,
        "weight": 5
      },
      "item-1543": {
        "value": 1,
        "weight": 4
      },
      "item-1544": {
        "value": 2,
        "weight": 3
      },
      "item-1545": {
        "value": 6,
        "weight": 6
      },
      "item-1546": {
        "value": 3,
        "weight": 4
      },
      "item-1547": {
        "value": 8,
        "weight": 5
      },
      "item-1548": {
        "value": 8,
        "weight": 1
      },
      "item-1549": {
        "value": 1,
        "weight": 7
      },
      "item-1550": {
        "value": 1,
        "weight": 1
      },
      "item-1551": {
        "value": 7,
        "weight": 1
      },
      "item-1552": {
        "value": 5,
        "weight": 3
      },
      "item-1553": {
        "value": 1,
        "weight": 4
      },
      "item-1554": {
        "value": 9,
        "weight": 3
      },
      "item-1555": {
        "value": 7,
        "weight": 4
      },
      "item-1556": {
        "value": 5,
        "weight": 9
      },
      "item-1557": {
        "value": 2,
        "weight": 2
      },
      "item-1558": {
        "value": 8,
        "weight": 2
      },
      "item-1559": {
        "value": 7,
        "weight": 6
      },
      "item-1560": {
        "value": 6,
        "weight": 8
      },
      "item-1561": {
        "value": 3,
        "weight": 6
      },
      "item-1562": {
        "value": 6,
        "weight": 3
      },
      "item-1563": {
        "value": 2,
        "weight": 3
      },
      "item-1564": {
        "value": 3,
        "weight": 5
      },
      "item-1565": {
        "value": 2,
        "weight": 2
      },
      "item-1566": {
        "value": 6,
        "weight": 2
      },
      "item-1567": {
        "value": 8,
        "weight": 6
      },
      "item-1568": {
        "value": 8,
        "weight": 9
      },
      "item-1569": {
        "value": 9,
        "weight": 3
      },
      "item-1570": {
        "value": 9,
        "weight": 5
      },
      "item-1571": {
        "value": 6,
        "weight": 6
      },
      "item-1572": {
        "value": 9,
        "weight": 7
      },
      "item-1573": {
        "value": 8,
        "weight": 7
      },
      "item-1574": {
        "value": 3,
        "weight": 1
      },
      "item-1575": {
        "value": 9,
        "weight": 2
      },
      "item-1576": {
        "value": 8,
        "weight": 4
      },
      "item-1577": {
        "value": 9,
        "weight": 4
      },
      "item-1578": {
        "value": 4,
        "weight": 7
      },
      "item-1579": {
        "value": 3,
        "weight": 9
      },
      "item-1580": {
        "value": 7,
        "weight": 9
      },
      "item-1581": {
        "value": 9,
        "weight": 9
      },
      "item-1582": {
        "value": 3,
        "weight": 8
      },
      "item-1583": {
        "value": 3,
        "weight": 6
      },
      "item-1584": {
        "value": 4,
        "weight": 8
      },
      "item-1585": {
        "value": 9,
        "weight": 9
      },
      "item-1586": {
        "value": 9,
        "weight": 2
      },
      "item-1587": {
        "value": 7,
        "weight": 4
      },
      "item-1588": {
        "value": 9,
        "weight": 6
      },
      "item-1589": {
        "value": 4,
        "weight": 9
      },
      "item-1590": {
        "value": 8,
        "weight": 5
      },
      "item-1591": {
        "value": 3,
        "weight": 8
      },
      "item-1592": {
        "value": 3,
        "weight": 7
      },
      "item-1593": {
        "value": 9,
        "weight": 5
      },
      "item-1594": {
        "value": 8,
        "weight": 4
      },
      "item-1595": {
        "value": 8,
        "weight": 4
      },
      "item-1596": {
        "value": 8,
        "weight": 7
      },
      "item-1597": {
        "value": 7,
        "weight": 4
      },
      "item-1598": {
        "value": 8,
        "weight": 9
      },
      "item-1599": {
        "value": 5,
        "weight": 4
      },
      "item-1600": {
        "value": 4,
        "weight": 7
      },
      "item-1601": {
        "value": 7,
        "weight": 9
      },
      "item-1602": {
        "value": 4,
        "weight": 3
      },
      "item-1603": {
        "value": 8,
        "weight": 3
      },
      "item-1604": {
        "value": 9,
        "weight": 6
      },
      "item-1605": {
        "value": 2,
        "weight": 6
      },
      "item-1606": {
        "value": 4,
        "weight": 3
      },
      "item-1607": {
        "value": 1,
        "weight": 1
      },
      "item-1608": {
        "value": 3,
        "weight": 4
      },
      "item-1609": {
        "value": 7,
        "weight": 2
      },
      "item-1610": {
        "value": 6,
        "weight": 4
      },
      "item-1611": {
        "value": 3,
        "weight": 5
      },
      "item-1612": {
        "value": 4,
        "weight": 7
      },
      "item-1613": {
        "value": 1,
        "weight": 5
      },
      "item-1614": {
        "value": 7,
        "weight": 2
      },
      "item-1615": {
        "value": 2,
        "weight": 6
      },
      "item-1616": {
        "value": 8,
        "weight": 5
      },
      "item-1617": {
        "value": 1,
        "weight": 9
      },
      "item-1618": {
        "value": 6,
        "weight": 4
      },
      "item-1619": {
        "value": 9,
        "weight": 4
      },
      "item-1620": {
        "value": 5,
        "weight": 7
      },
      "item-1621": {
        "value": 5,
        "weight": 5
      },
      "item-1622": {
        "value": 7,
        "weight": 2
      },
      "item-1623": {
        "value": 7,
        "weight": 1
      },
      "item-1624": {
        "value": 3,
        "weight": 1
      },
      "item-1625": {
        "value": 5,
        "weight": 8
      },
      "item-1626": {
        "value": 5,
        "weight": 6
      },
      "item-1627": {
        "value": 8,
        "weight": 5
      },
      "item-1628": {
        "value": 8,
        "weight": 8
      },
      "item-1629": {
        "value": 4,
        "weight": 2
      },
      "item-1630": {
        "value": 6,
        "weight": 5
      },
      "item-1631": {
        "value": 6,
        "weight": 3
      },
      "item-1632": {
        "value": 3,
        "weight": 6
      },
      "item-1633": {
        "value": 6,
        "weight": 7
      },
      "item-1634": {
        "value": 7,
        "weight": 6
      },
      "item-1635": {
        "value": 2,
        "weight": 3
      },
      "item-1636": {
        "value": 3,
        "weight": 6
      },
      "item-1637": {
        "value": 5,
        "weight": 6
      },
      "item-1638": {
        "value": 3,
        "weight": 3
      },
      "item-1639": {
        "value": 6,
        "weight": 2
      },
      "item-1640": {
        "value": 1,
        "weight": 1
      },
      "item-1641": {
        "value": 3,
        "weight": 5
      },
      "item-1642": {
        "value": 1,
        "weight": 3
      },
      "item-1643": {
        "value": 6,
        "weight": 4
      },
      "item-1644": {
        "value": 5,
        "weight": 4
      },
      "item-1645": {
        "value": 1,
        "weight": 7
      },
      "item-1646": {
        "value": 6,
        "weight": 1
      },
      "item-1647": {
        "value": 9,
        "weight": 2
      },
      "item-1648": {
        "value": 7,
        "weight": 2
      },
      "item-1649": {
        "value": 8,
        "weight": 1
      },
      "item-1650": {
        "value": 7,
        "weight": 5
      },
      "item-1651": {
        "value": 8,
        "weight": 9
      },
      "item-1652": {
        "value": 7,
        "weight": 3
      },
      "item-1653": {
        "value": 5,
        "weight": 9
      },
      "item-1654": {
        "value": 2,
        "weight": 2
      },
      "item-1655": {
        "value": 2,
        "weight": 4
      },
      "item-1656": {
        "value": 6,
        "weight": 5
      },
      "item-1657": {
        "value": 5,
        "weight": 9
      },
      "item-1658": {
        "value": 4,
        "weight": 1
      },
      "item-1659": {
        "value": 2,
        "weight": 6
      },
      "item-1660": {
        "value": 1,
        "weight": 6
      },
      "item-1661": {
        "value": 7,
        "weight": 5
      },
      "item-1662": {
        "value": 8,
        "weight": 5
      },
      "item-1663": {
        "value": 9,
        "weight": 1
      },
      "item-1664": {
        "value": 9,
        "weight": 5
      },
      "item-1665": {
        "value": 6,
        "weight": 5
      },
      "item-1666": {
        "value": 4,
        "weight": 4
      },
      "item-1667": {
        "value": 3,
        "weight": 9
      },
      "item-1668": {
        "value": 1,
        "weight": 5
      },
      "item-1669": {
        "value": 3,
        "weight": 7
      },
      "item-1670": {
        "value": 1,
        "weight": 5
      },
      "item-1671": {
        "value": 6,
        "weight": 2
      },
      "item-1672": {
        "value": 7,
        "weight": 1
      },
      "item-1673": {
        "value": 6,
        "weight": 4
      },
      "item-1674": {
        "value": 3,
        "weight": 2
      },
      "item-1675": {
        "value": 4,
        "weight": 7
      },
      "item-1676": {
        "value": 1,
        "weight": 5
      },
      "item-1677": {
        "value": 4,
        "weight": 8
      },
      "item-1678": {
        "value": 7,
        "weight": 1
      },
      "item-1679": {
        "value": 6,
        "weight": 2
      },
      "item-1680": {
        "value": 2,
        "weight": 7
      },
      "item-1681": {
        "value": 9,
        "weight": 5
      },
      "item-1682": {
        "value": 8,
        "weight": 3
      },
      "item-1683": {
        "value": 1,
        "weight": 6
      },
      "item-1684": {
        "value": 4,
        "weight": 7
      },
      "item-1685": {
        "value": 5,
        "weight": 8
      },
      "item-1686": {
        "value": 5,
        "weight": 3
      },
      "item-1687": {
        "value": 8,
        "weight": 9
      },
      "item-1688": {
        "value": 2,
        "weight": 4
      },
      "item-1689": {
        "value": 9,
        "weight": 8
      },
      "item-1690": {
        "value": 3,
        "weight": 6
      },
      "item-1691": {
        "value": 1,
        "weight": 5
      },
      "item-1692": {
        "value": 3,
        "weight": 9
      },
      "item-1693": {
        "value": 6,
        "weight": 6
      },
      "item-1694": {
        "value": 7,
        "weight": 9
      },
      "item-1695": {
        "value": 4,
        "weight": 9
      },
      "item-1696": {
        "value": 1,
        "weight": 1
      },
      "item-1697": {
        "value": 3,
        "weight": 4
      },
      "item-1698": {
        "value": 2,
        "weight": 3
      },
      "item-1699": {
        "value": 5,
        "weight": 4
      },
      "item-1700": {
        "value": 3,
        "weight": 6
      },
      "item-1701": {
        "value": 4,
        "weight": 4
      },
      "item-1702": {
        "value": 7,
        "weight": 9
      },
      "item-1703": {
        "value": 7,
        "weight": 3
      },
      "item-1704": {
        "value": 5,
        "weight": 4
      },
      "item-1705": {
        "value": 7,
        "weight": 3
      },
      "item-1706": {
        "value": 3,
        "weight": 4
      },
      "item-1707": {
        "value": 1,
        "weight": 3
      },
      "item-1708": {
        "value": 7,
        "weight": 4
      },
      "item-1709": {
        "value": 8,
        "weight": 5
      },
      "item-1710": {
        "value": 2,
        "weight": 8
      },
      "item-1711": {
        "value": 5,
        "weight": 7
      },
      "item-1712": {
        "value": 2,
        "weight": 5
      },
      "item-1713": {
        "value": 8,
        "weight": 5
      },
      "item-1714": {
        "value": 5,
        "weight": 9
      },
      "item-1715": {
        "value": 6,
        "weight": 4
      },
      "item-1716": {
        "value": 3,
        "weight": 2
      },
      "item-1717": {
        "value": 5,
        "weight": 4
      },
      "item-1718": {
        "value": 6,
        "weight": 5
      },
      "item-1719": {
        "value": 3,
        "weight": 4
      },
      "item-1720": {
        "value": 4,
        "weight": 8
      },
      "item-1721": {
        "value": 1,
        "weight": 4
      },
      "item-1722": {
        "value": 5,
        "weight": 1
      },
      "item-1723": {
        "value": 7,
        "weight": 2
      },
      "item-1724": {
        "value": 9,
        "weight": 3
      },
      "item-1725": {
        "value": 3,
        "weight": 5
      },
      "item-1726": {
        "value": 8,
        "weight": 3
      },
      "item-1727": {
        "value": 1,
        "weight": 6
      },
      "item-1728": {
        "value": 4,
        "weight": 7
      },
      "item-1729": {
        "value": 3,
        "weight": 1
      },
      "item-1730": {
        "value": 8,
        "weight": 3
      },
      "item-1731": {
        "value": 3,
        "weight": 9
      },
      "item-1732": {
        "value": 2,
        "weight": 8
      },
      "item-1733": {
        "value": 6,
        "weight": 8
      },
      "item-1734": {
        "value": 1,
        "weight": 5
      },
      "item-1735": {
        "value": 6,
        "weight": 9
      },
      "item-1736": {
        "value": 5,
        "weight": 4
      },
      "item-1737": {
        "value": 4,
        "weight": 6
      },
      "item-1738": {
        "value": 3,
        "weight": 9
      },
      "item-1739": {
        "value": 4,
        "weight": 3
      },
      "item-1740": {
        "value": 1,
        "weight": 9
      },
      "item-1741": {
        "value": 4,
        "weight": 1
      },
      "item-1742": {
        "value": 7,
        "weight": 1
      },
      "item-1743": {
        "value": 1,
        "weight": 7
      },
      "item-1744": {
        "value": 8,
        "weight": 1
      },
      "item-1745": {
        "value": 4,
        "weight": 5
      },
      "item-1746": {
        "value": 5,
        "weight": 2
      },
      "item-1747": {
        "value": 2,
        "weight": 2
      },
      "item-1748": {
        "value": 7,
        "weight": 6
      },
      "item-1749": {
        "value": 2,
        "weight": 2
      },
      "item-1750": {
        "value": 7,
        "weight": 4
      },
      "item-1751": {
        "value": 4,
        "weight": 4
      },
      "item-1752": {
        "value": 6,
        "weight": 8
      },
      "item-1753": {
        "value": 5,
        "weight": 2
      },
      "item-1754": {
        "value": 4,
        "weight": 2
      },
      "item-1755": {
        "value": 6,
        "weight": 3
      },
      "item-1756": {
        "value": 8,
        "weight": 5
      },
      "item-1757": {
        "value": 5,
        "weight": 2
      },
      "item-1758": {
        "value": 6,
        "weight": 3
      },
      "item-1759": {
        "value": 7,
        "weight": 8
      },
      "item-1760": {
        "value": 2,
        "weight": 8
      },
      "item-1761": {
        "value": 5,
        "weight": 3
      },
      "item-1762": {
        "value": 4,
        "weight": 8
      },
      "item-1763": {
        "value": 1,
        "weight": 5
      },
      "item-1764": {
        "value": 7,
        "weight": 1
      },
      "item-1765": {
        "value": 3,
        "weight": 4
      },
      "item-1766": {
        "value": 7,
        "weight": 8
      },
      "item-1767": {
        "value": 4,
        "weight": 2
      },
      "item-1768": {
        "value": 1,
        "weight": 9
      },
      "item-1769": {
        "value": 4,
        "weight": 4
      },
      "item-1770": {
        "value": 2,
        "weight": 1
      },
      "item-1771": {
        "value": 2,
        "weight": 5
      },
      "item-1772": {
        "value": 3,
        "weight": 6
      },
      "item-1773": {
        "value": 7,
        "weight": 2
      },
      "item-1774": {
        "value": 2,
        "weight": 7
      },
      "item-1775": {
        "value": 8,
        "weight": 5
      },
      "item-1776": {
        "value": 1,
        "weight": 1
      },
      "item-1777": {
        "value": 7,
        "weight": 7
      },
      "item-1778": {
        "value": 5,
        "weight": 4
      },
      "item-1779": {
        "value": 8,
        "weight": 7
      },
      "item-1780": {
        "value": 1,
        "weight": 8
      },
      "item-1781": {
        "value": 4,
        "weight": 8
      },
      "item-1782": {
        "value": 7,
        "weight": 5
      },
      "item-1783": {
        "value": 8,
        "weight": 4
      },
      "item-1784": {
        "value": 2,
        "weight": 9
      },
      "item-1785": {
        "value": 2,
        "weight": 4
      },
      "item-1786": {
        "value": 5,
        "weight": 5
      },
      "item-1787": {
        "value": 7,
        "weight": 4
      },
      "item-1788": {
        "value": 3,
        "weight": 7
      },
      "item-1789": {
        "value": 9,
        "weight": 2
      },
      "item-1790": {
        "value": 8,
        "weight": 4
      },
      "item-1791": {
        "value": 4,
        "weight": 3
      },
      "item-1792": {
        "value": 3,
        "weight": 7
      },
      "item-1793": {
        "value": 4,
        "weight": 4
      },
      "item-1794": {
        "value": 9,
        "weight": 3
      },
      "item-1795": {
        "value": 1,
        "weight": 4
      },
      "item-1796": {
        "value": 6,
        "weight": 7
      },
      "item-1797": {
        "value": 5,
        "weight": 9
      },
      "item-1798": {
        "value": 7,
        "weight": 5
      },
      "item-1799": {
        "value": 7,
        "weight": 1
      },
      "item-1800": {
        "value": 2,
        "weight": 9
      },
      "item-1801": {
        "value": 7,
        "weight": 1
      },
      "item-1802": {
        "value": 6,
        "weight": 2
      },
      "item-1803": {
        "value": 5,
        "weight": 5
      },
      "item-1804": {
        "value": 9,
        "weight": 5
      },
      "item-1805": {
        "value": 4,
        "weight": 6
      },
      "item-1806": {
        "value": 4,
        "weight": 6
      },
      "item-1807": {
        "value": 2,
        "weight": 6
      },
      "item-1808": {
        "value": 2,
        "weight": 5
      },
      "item-1809": {
        "value": 1,
        "weight": 9
      },
      "item-1810": {
        "value": 5,
        "weight": 8
      },
      "item-1811": {
        "value": 1,
        "weight": 9
      },
      "item-1812": {
        "value": 3,
        "weight": 1
      },
      "item-1813": {
        "value": 3,
        "weight": 9
      },
      "item-1814": {
        "value": 6,
        "weight": 4
      },
      "item-1815": {
        "value": 5,
        "weight": 5
      },
      "item-1816": {
        "value": 4,
        "weight": 5
      },
      "item-1817": {
        "value": 6,
        "weight": 4
      },
      "item-1818": {
        "value": 6,
        "weight": 1
      },
      "item-1819": {
        "value": 1,
        "weight": 9
      },
      "item-1820": {
        "value": 4,
        "weight": 1
      },
      "item-1821": {
        "value": 9,
        "weight": 8
      },
      "item-1822": {
        "value": 4,
        "weight": 6
      },
      "item-1823": {
        "value": 2,
        "weight": 2
      },
      "item-1824": {
        "value": 6,
        "weight": 1
      },
      "item-1825": {
        "value": 4,
        "weight": 2
      },
      "item-1826": {
        "value": 4,
        "weight": 9
      },
      "item-1827": {
        "value": 6,
        "weight": 5
      },
      "item-1828": {
        "value": 2,
        "weight": 2
      },
      "item-1829": {
        "value": 8,
        "weight": 6
      },
      "item-1830": {
        "value": 4,
        "weight": 9
      },
      "item-1831": {
        "value": 2,
        "weight": 2
      },
      "item-1832": {
        "value": 6,
        "weight": 9
      },
      "item-1833": {
        "value": 7,
        "weight": 3
      },
      "item-1834": {
        "value": 3,
        "weight": 9
      },
      "item-1835": {
        "value": 5,
        "weight": 3
      },
      "item-1836": {
        "value": 9,
        "weight": 9
      },
      "item-1837": {
        "value": 8,
        "weight": 6
      },
      "item-1838": {
        "value": 2,
        "weight": 7
      },
      "item-1839": {
        "value": 2,
        "weight": 4
      },
      "item-1840": {
        "value": 2,
        "weight": 7
      },
      "item-1841": {
        "value": 5,
        "weight": 9
      },
      "item-1842": {
        "value": 5,
        "weight": 9
      },
      "item-1843": {
        "value": 1,
        "weight": 7
      },
      "item-1844": {
        "value": 7,
        "weight": 2
      },
      "item-1845": {
        "value": 9,
        "weight": 8
      },
      "item-1846": {
        "value": 7,
        "weight": 7
      },
      "item-1847": {
        "value": 3,
        "weight": 9
      },
      "item-1848": {
        "value": 5,
        "weight": 5
      },
      "item-1849": {
        "value": 9,
        "weight": 1
      },
      "item-1850": {
        "value": 1,
        "weight": 8
      },
      "item-1851": {
        "value": 2,
        "weight": 7
      },
      "item-1852": {
        "value": 9,
        "weight": 3
      },
      "item-1853": {
        "value": 8,
        "weight": 1
      },
      "item-1854": {
        "value": 2,
        "weight": 1
      },
      "item-1855": {
        "value": 4,
        "weight": 2
      },
      "item-1856": {
        "value": 6,
        "weight": 6
      },
      "item-1857": {
        "value": 4,
        "weight": 7
      },
      "item-1858": {
        "value": 1,
        "weight": 7
      },
      "item-1859": {
        "value": 5,
        "weight": 9
      },
      "item-1860": {
        "value": 9,
        "weight": 9
      },
      "item-1861": {
        "value": 2,
        "weight": 1
      },
      "item-1862": {
        "value": 8,
        "weight": 9
      },
      "item-1863": {
        "value": 5,
        "weight": 5
      },
      "item-1864": {
        "value": 1,
        "weight": 9
      },
      "item-1865": {
        "value": 6,
        "weight": 3
      },
      "item-1866": {
        "value": 9,
        "weight": 8
      },
      "item-1867": {
        "value": 6,
        "weight": 9
      },
      "item-1868": {
        "value": 1,
        "weight": 9
      },
      "item-1869": {
        "value": 4,
        "weight": 2
      },
      "item-1870": {
        "value": 1,
        "weight": 8
      },
      "item-1871": {
        "value": 7,
        "weight": 7
      },
      "item-1872": {
        "value": 6,
        "weight": 5
      },
      "item-1873": {
        "value": 5,
        "weight": 2
      },
      "item-1874": {
        "value": 3,
        "weight": 2
      },
      "item-1875": {
        "value": 3,
        "weight": 3
      },
      "item-1876": {
        "value": 4,
        "weight": 6
      },
      "item-1877": {
        "value": 9,
        "weight": 3
      },
      "item-1878": {
        "value": 4,
        "weight": 5
      },
      "item-1879": {
        "value": 4,
        "weight": 5
      },
      "item-1880": {
        "value": 4,
        "weight": 3
      },
      "item-1881": {
        "value": 6,
        "weight": 5
      },
      "item-1882": {
        "value": 9,
        "weight": 7
      },
      "item-1883": {
        "value": 7,
        "weight": 4
      },
      "item-1884": {
        "value": 5,
        "weight": 3
      },
      "item-1885": {
        "value": 7,
        "weight": 7
      },
      "item-1886": {
        "value": 2,
        "weight": 7
      },
      "item-1887": {
        "value": 5,
        "weight": 6
      },
      "item-1888": {
        "value": 3,
        "weight": 6
      },
      "item-1889": {
        "value": 5,
        "weight": 5
      },
      "item-1890": {
        "value": 1,
        "weight": 2
      },
      "item-1891": {
        "value": 1,
        "weight": 7
      },
      "item-1892": {
        "value": 4,
        "weight": 9
      },
      "item-1893": {
        "value": 6,
        "weight": 9
      },
      "item-1894": {
        "value": 9,
        "weight": 2
      },
      "item-1895": {
        "value": 5,
        "weight": 7
      },
      "item-1896": {
        "value": 6,
        "weight": 6
      },
      "item-1897": {
        "value": 8,
        "weight": 9
      },
      "item-1898": {
        "value": 3,
        "weight": 7
      },
      "item-1899": {
        "value": 3,
        "weight": 6
      },
      "item-1900": {
        "value": 4,
        "weight": 8
      },
      "item-1901": {
        "value": 5,
        "weight": 6
      },
      "item-1902": {
        "value": 3,
        "weight": 8
      },
      "item-1903": {
        "value": 1,
        "weight": 8
      },
      "item-1904": {
        "value": 6,
        "weight": 2
      },
      "item-1905": {
        "value": 9,
        "weight": 3
      },
      "item-1906": {
        "value": 8,
        "weight": 2
      },
      "item-1907": {
        "value": 3,
        "weight": 5
      },
      "item-1908": {
        "value": 6,
        "weight": 2
      },
      "item-1909": {
        "value": 3,
        "weight": 7
      },
      "item-1910": {
        "value": 7,
        "weight": 4
      },
      "item-1911": {
        "value": 3,
        "weight": 6
      },
      "item-1912": {
        "value": 2,
        "weight": 4
      },
      "item-1913": {
        "value": 9,
        "weight": 1
      },
      "item-1914": {
        "value": 2,
        "weight": 8
      },
      "item-1915": {
        "value": 9,
        "weight": 4
      },
      "item-1916": {
        "value": 2,
        "weight": 1
      },
      "item-1917": {
        "value": 7,
        "weight": 8
      },
      "item-1918": {
        "value": 7,
        "weight": 4
      },
      "item-1919": {
        "value": 7,
        "weight": 3
      },
      "item-1920": {
        "value": 6,
        "weight": 8
      },
      "item-1921": {
        "value": 7,
        "weight": 6
      },
      "item-1922": {
        "value": 7,
        "weight": 3
      },
      "item-1923": {
        "value": 2,
        "weight": 1
      },
      "item-1924": {
        "value": 5,
        "weight": 1
      },
      "item-1925": {
        "value": 8,
        "weight": 7
      },
      "item-1926": {
        "value": 1,
        "weight": 7
      },
      "item-1927": {
        "value": 9,
        "weight": 9
      },
      "item-1928": {
        "value": 7,
        "weight": 6
      },
      "item-1929": {
        "value": 8,
        "weight": 1
      },
      "item-1930": {
        "value": 1,
        "weight": 7
      },
      "item-1931": {
        "value": 8,
        "weight": 6
      },
      "item-1932": {
        "value": 1,
        "weight": 6
      },
      "item-1933": {
        "value": 5,
        "weight": 1
      },
      "item-1934": {
        "value": 2,
        "weight": 7
      },
      "item-1935": {
        "value": 8,
        "weight": 2
      },
      "item-1936": {
        "value": 8,
        "weight": 7
      },
      "item-1937": {
        "value": 3,
        "weight": 6
      },
      "item-1938": {
        "value": 5,
        "weight": 3
      },
      "item-1939": {
        "value": 2,
        "weight": 8
      },
      "item-1940": {
        "value": 8,
        "weight": 8
      },
      "item-1941": {
        "value": 3,
        "weight": 3
      },
      "item-1942": {
        "value": 4,
        "weight": 4
      },
      "item-1943": {
        "value": 1,
        "weight": 5
      },
      "item-1944": {
        "value": 1,
        "weight": 9
      },
      "item-1945": {
        "value": 2,
        "weight": 1
      },
      "item-1946": {
        "value": 8,
        "weight": 6
      },
      "item-1947": {
        "value": 4,
        "weight": 5
      },
      "item-1948": {
        "value": 4,
        "weight": 1
      },
      "item-1949": {
        "value": 6,
        "weight": 8
      },
      "item-1950": {
        "value": 6,
        "weight": 4
      },
      "item-1951": {
        "value": 2,
        "weight": 2
      },
      "item-1952": {
        "value": 8,
        "weight": 6
      },
      "item-1953": {
        "value": 3,
        "weight": 7
      },
      "item-1954": {
        "value": 2,
        "weight": 1
      },
      "item-1955": {
        "value": 4,
        "weight": 8
      },
      "item-1956": {
        "value": 1,
        "weight": 4
      },
      "item-1957": {
        "value": 4,
        "weight": 8
      },
      "item-1958": {
        "value": 1,
        "weight": 9
      },
      "item-1959": {
        "value": 3,
        "weight": 1
      },
      "item-1960": {
        "value": 5,
        "weight": 4
      },
      "item-1961": {
        "value": 9,
        "weight": 2
      }
    }
  }
print(knapsack.keys())

solution = solveKnapsack2(knapsack)

print(solution.keys())
totalValue = solution["totalValue"]
totalWeight = solution["totalWeight"]
rejectedItemIds = solution["rejectedItemIds"]
selectedItemIds = solution["selectedItemIds"]

assert(len(rejectedItemIds) > 1)
assert(len(selectedItemIds) > 1)

print("totalValue", totalValue)
print("totalWeight", totalWeight)
print("selectedItemIds", selectedItemIds)
print("rejectedItemsIds", rejectedItemIds)

print("ok")