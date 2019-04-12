#   div.viewed-search:nth-child(5) div.container:nth-child(3) div.row div.contentpart.col-sm-12.col-md-9:nth-child(2) div.tab-content.active:nth-child(4) div.tab-pane.row.active > div.search-results.hide-in-toggle:nth-child(5)


def hasNoResults(driver):
    noResultsPath = "div.no-result-message "
    return False if driver.find_element_by_css_selector(
        noResultsPath).get_attribute("style") == "display: none;" else True
