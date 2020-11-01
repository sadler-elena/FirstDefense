def websiteScan(submittedURL):
    # Import modules
    import sys
    import requests
    from urllib.parse import urlparse
    from bs4 import BeautifulSoup

    # Common phishing word keylist:
    commonPhishingWords = ["Request", "Legal", "Compromise", "Urgent", "Payment", "Status", "Direct", "Expenses",
                           "Payroll", "Card", "Due", "Expiration", "Reset"]
    commonPhishingWordsFound = 0

    # Initialize variables that will be used to export report.
    # 0 = no; 1 = yes; 3 = unsure (string)
    # Able to connect?
    ableToConnect = "1"
    # Does site use HTTPS?
    siteUsesHTTPS = "0"
    # Site has too many redirects
    tooManyRedirects = "0"
    # Took too long to connect
    timeOutError = "0"
    # Possibly phishing site
    possiblyPhishing = "0"
    # Does the actual domain match the targeted one?
    targetDomainIsDisplayed = "0"

    def assessPhishingThreat(phishingWordCount):
        if phishingWordCount < 5:
            return "0"
        if phishingWordCount > 5:
            return "1"

    # Take URL from request
    inputURL = submittedURL

    # Test connection to site:
    try:
        site = requests.get(inputURL, timeout=3)
    except requests.exceptions.HTTPError:
        ableToConnect = "0"
        successfulConnection = False
    except requests.exceptions.Timeout:
        timeOutError = "1"
        successfulConnection = False
    except requests.exceptions.TooManyRedirects:
        tooManyRedirects = "1"
        successfulConnection = False
    except requests.exceptions.RequestException:
        ableToConnect = "0"
        successfulConnection = False
    else:
        successfulConnection = True

    if successfulConnection:
        inputURLParts = urlparse(inputURL)
        targetUrlParts = urlparse(site.url)
        # Check for use of HTTPS:
        if targetUrlParts.scheme == "https":
            siteUsesHTTPS = "1"
        # Checks that the displayed domain name is the same as the target destination.
        if inputURLParts.netloc == targetUrlParts.netloc:
            targetDomainIsDisplayed = "1"
        # Scan title for fishing keywords
        soup = BeautifulSoup(site.content, 'html.parser')
        titleElements = soup.find_all('title')
        headingElements = soup.find_all('h1')
        for word in headingElements:
            for phishingWord in commonPhishingWords:
                wordSearch = word.text.find(phishingWord)
                if wordSearch != -1:
                    commonPhishingWordsFound += 1
        for word in titleElements:
            for phishingWord in commonPhishingWords:
                wordSearch = word.text.find(phishingWord)
                if wordSearch != -1:
                    commonPhishingWordsFound += 1
        possiblyPhishing = assessPhishingThreat(commonPhishingWordsFound)
    # Each number in code represents a characteristic of the site.
    # [0]-Able to connect?, [1]- Does site use HTTPS? [2]- are Too Many Redirects? [3]- did TimeOutError? [4]- is Possibly Phishing?

    reportCode = ableToConnect + siteUsesHTTPS + tooManyRedirects + timeOutError + possiblyPhishing

    return reportCode


