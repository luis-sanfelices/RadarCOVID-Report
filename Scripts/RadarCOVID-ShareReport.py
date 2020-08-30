import os

import tweepy


def _share_radar_covid_report_to_twitter():
    enable_share_to_twitter = os.environ["RADARCOVID_REPORT__ENABLE_SHARE_TO_TWITTER"]

    if not enable_share_to_twitter:
        return

    twitter_api_auth_keys = os.environ["RADARCOVID_REPORT__TWITTER_API_AUTH_KEYS"]
    twitter_api_auth_keys = twitter_api_auth_keys.split(":")
    auth = tweepy.OAuthHandler(twitter_api_auth_keys[0], twitter_api_auth_keys[1])
    auth.set_access_token(twitter_api_auth_keys[2], twitter_api_auth_keys[3])

    api = tweepy.API(auth)
    api.update_status("Hello Tweepy")


if __name__ == "__main__":
    print(dict(os.environ))
    _share_radar_covid_report_to_twitter()
