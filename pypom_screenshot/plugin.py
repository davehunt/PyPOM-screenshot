# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pypom import hookimpl


@hookimpl
def pypom_after_wait_for_page_to_load(page):
    page.selenium.get_screenshot_as_file(page.__class__.__name__ + '.png')


@hookimpl
def pypom_after_wait_for_region_to_load(region):
    region.root.screenshot(region.__class__.__name__ + '.png')
