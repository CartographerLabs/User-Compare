from PIL import Image
from fuzzywuzzy import fuzz
from pixelmatch.contrib.PIL import pixelmatch


class user():
    # Define the properties that a user has
    username = ""
    name = ""
    profile_picture_dst = ""
    bio = ""
    list_of_posts = []
    location = ""
    dob = ""
    urls = []
    following = []
    followers = []

    def __init__(self, username, profile_picture_dst, bio, list_of_posts, location, dob, urls, following, followers, name):
        """
        Creates a new user object.

        Args:
        username (str): The username of the user.
        profile_picture_dst (str): The path to the user's profile picture.
        bio (str): The user's bio.
        list_of_posts (list of str): A list of the user's posts.
        location (str): The user's location.
        dob (str): The user's date of birth.
        urls (list of str): A list of URLs associated with the user.
        following (list of str): A list of users that the user is following.
        followers (list of str): A list of users that follow the user.
        name (str): The user's name.
        """
        self.username = username
        self.profile_picture_dst = profile_picture_dst
        self.bio = bio
        self.list_of_posts = list_of_posts
        self.location = location
        self.dob = dob
        self.urls = urls
        self.following = following
        self.followers = followers
        self.name = name


    def _compare_username(self, other_username):
        """
        Compares the user's username to another username and returns a fuzzy match score.

        Args:
        other_username (str): The username to compare against.

        Returns:
        A fuzzy match score as an integer.
        """
        fuzz_ratio = fuzz.partial_ratio(self.username.lower(), other_username.lower())

        return fuzz_ratio

    def _compare_name(self, other_name):
        """
        Compares the user's name to another name and returns a fuzzy match score.

        Args:
        other_name (str): The name to compare against.

        Returns:
        A fuzzy match score as an integer.
        """
        fuzz_ratio = fuzz.partial_ratio(self.name.lower(), other_name.lower())

        return fuzz_ratio

    def _compare_posts(self, other_posts):
        """
        Compares the user's list of posts to another list of posts and returns the highest fuzzy match score.

        Args:
        other_posts (list of str): The list of posts to compare against.

        Returns:
        The highest fuzzy match score as an integer.
        """
        highest_post_similarity = 0
        for this_post in self.list_of_posts:
            for other_post in other_posts:
                fuzz_ratio = fuzz.ratio(this_post.lower(), other_post.lower())

                if fuzz_ratio > highest_post_similarity:
                    highest_post_similarity = fuzz_ratio

        return highest_post_similarity


    def _compare_dob(self, other_dob):
        """
        Compares the user's date of birth to another date of birth and returns a match score.

        Args:
        other_dob (str): The date of birth to compare against.

        Returns:
        A match score as an integer.
        """
        if self.dob == other_dob:
            return 100
        else:
            return  0

    def _compare_profile_picture(self, other_picture):
        """
        Compare the profile picture of two users and return a percentage match.

        Parameters:
        self.profile_picture_dst (str): path to the profile picture of the current user
        other_picture (str): path to the profile picture of the other user

        Returns:
        match (float): percentage match between the two profile pictures
        """

        # Opening the two images
        img_a = Image.open(self.profile_picture_dst)
        img_b = Image.open(other_picture)

        # Creating a new image with the same size as the two images
        img_diff = Image.new("RGBA", img_a.size)

        # Comparing the two images
        mismatch = pixelmatch(img_a, img_b, img_diff, includeAA=True)

        # Calculating the match percentage
        size = img_b.size[0] * img_b.size[1]
        percentage = 100 * float(mismatch) / float(size)
        match = 100 - percentage

        return match


    def _compare_bio(self, other_bio):
        """
        Compare the biography of two users and return a fuzz ratio.

        Parameters:
        self.bio (str): biography of the current user
        other_bio (str): biography of the other user

        Returns:
        fuzz_ratio (int): fuzz ratio between the two biographies
        """

        # Calculating the fuzz ratio of the two biographies
        fuzz_ratio = fuzz.partial_ratio(self.bio.lower(), other_bio.lower())

        return fuzz_ratio


    def _compare_urls(self, other_urls):
        """
        Compare the URLs of two users and return the highest similarity ratio.

        Parameters:
        self.urls (list): list of URLs of the current user
        other_urls (list): list of URLs of the other user

        Returns:
        highest_url_similarity (int): highest similarity ratio between the two lists of URLs
        """

        # Initializing the highest URL similarity to zero
        highest_url_similarity = 0

        # Looping through the URLs of the current user
        for this_url in self.urls:
            # Looping through the URLs of the other user
            for other_url in other_urls:
                # Calculating the fuzz ratio between the two URLs
                fuzz_ratio = fuzz.ratio(this_url.lower(), other_url.lower())

                # Updating the highest URL similarity if necessary
                if fuzz_ratio > highest_url_similarity:
                    highest_url_similarity = fuzz_ratio

        return highest_url_similarity


    def _compare_followers(self, other_followers):
        """
        Compare the followers of two users and return a percentage of users in common.

        Parameters:
        self.followers (list): list of usernames of the current user's followers
        other_followers (list): list of usernames of the other user's followers

        Returns:
        percentage (float): percentage of users in common between the two lists of followers
        """

        # Converting the other followers list to lowercase
        other_followers = [x.lower() for x in other_followers]

        # Initializing the number of common followers to zero
        number_between = 0

        # Looping through the followers of the current user
        for username in self.followers:
            # Incrementing the number of common followers if the username is in the other followers list
            if username.lower() in other_followers:
                number_between = number_between + 1

        # Calculating the percentage of common followers
        percentage = 100 * float(number_between) / float(len(self.followers))

        return percentage

    def _compare_following(self, other_following):
        """
        Compares the list of users that this user is following with another list of users
        to determine how many users are in common and returns the percentage of similarity.
        :param other_following: a list of users that we want to compare to this user's list of following
        :return: percentage of similarity as a float
        """
        other_following = [x.lower() for x in other_following]    # convert all usernames to lowercase for easier comparison
        number_between = 0                                       # count of users in common
        for username in self.following:
            if username.lower() in other_following:              # if the username is in the other list, increment number_between
                number_between = number_between + 1

        percentage = 100 * float(number_between) / float(len(self.following))   # calculate the percentage of similarity
        return percentage

    def _compare_location(self, other_location):
        for location in self.location:
            if location in other_location:
                return 100

        return 0

    def is_same(self, comparison_user):
        confidence_scores = []

        if comparison_user.location != None and self.location != None:
            location_confidence = self._compare_location(comparison_user.location)
            confidence_scores.append(location_confidence)

        if comparison_user.username != None and self.username != None:
            username_confidence = self._compare_username(comparison_user.username)
            confidence_scores.append(username_confidence)

        if comparison_user.profile_picture_dst != None and self.profile_picture_dst != None:
            profile_picture_confidence = self._compare_profile_picture(comparison_user.profile_picture_dst)
            confidence_scores.append(profile_picture_confidence)

        if comparison_user.bio != None and self.bio != None:
            bio_confidence = self._compare_bio(comparison_user.bio)
            confidence_scores.append(bio_confidence)

        if comparison_user.list_of_posts != None and self.list_of_posts != None:
            post_confidence = self._compare_posts(comparison_user.list_of_posts)
            confidence_scores.append(post_confidence)

        if comparison_user.dob != None and self.dob != None:
            dob_confidence = self._compare_dob(comparison_user.dob)
            confidence_scores.append(dob_confidence)

        if comparison_user.urls != None and self.urls != None:
            url_confidence = self._compare_urls(comparison_user.urls)
            confidence_scores.append(url_confidence)

        if comparison_user.following != None and self.following != None:
            following_confidence = self._compare_following(comparison_user.following)
            confidence_scores.append(following_confidence)

        if comparison_user.followers != None and self.followers != None:
            followers_confidence = self._compare_followers(comparison_user.followers)
            confidence_scores.append(followers_confidence)

        if comparison_user.name != None and self.name != None:
            name_confidence = self._compare_name(comparison_user.name)
            confidence_scores.append(name_confidence)

        if confidence_scores:
            average_confidence = sum(confidence_scores) / len(confidence_scores)
        else:
            average_confidence = 0

        return average_confidence


