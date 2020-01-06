## unhappy gaming path 1
  * greet
   - utter_greet
  * mood_feel_bad
    - utter_feel_bad
    - utter_ask_talk
  * talk_topic_gaming{"topic": "gaming"}
    - slot{"topic": "gaming"}
    - utter_ask_gaming
  * deny
    - utter_happy
    - utter_ask_talk_anything_else

## happy gaming path 1
  * greet
    - utter_greet
  * mood_feel_good OR affirm
    - utter_happy
    - utter_ask_about_day
  * mood_feel_good OR affirm
    - utter_day_happy
    - utter_ask_talk
  * talk_topic_gaming{"topic": "gaming"}
    - slot{"topic": "gaming"}
    - utter_ask_gaming
  * affirm
    - utter_like_gaming
    - utter_ask_platform
  * platform_console
    - utter_console
    - utter_ask_console
  * console_xbox
    - utter_xbox
    - utter_ask_talk_anything_else

## happy gaming path 2
  * talk_topic_gaming{"topic": "gaming"}
    - slot{"topic": "gaming"}
    - utter_ask_gaming
  * affirm
    - utter_like_gaming
    - utter_ask_platform
  * platform_pc
    - utter_pc
    - utter_ask_talk_anything_else

## happy gaming path 3
  * talk_topic_gaming{"topic": "gaming"}
    - slot{"topic": "gaming"}
    - utter_ask_gaming
  * affirm
    - utter_like_gaming
    - utter_ask_platform
  * platform_console
    - utter_console
    - utter_ask_console
  * console_playstation
    - utter_playstation
    - utter_ask_talk_anything_else

## happy gaming path 4
  * talk_topic_gaming{"topic": "gaming"}
    - slot{"topic": "gaming"}
    - utter_ask_gaming
  * affirm
    - utter_like_gaming
    - utter_ask_platform
  * platform_console
    - utter_console
    - utter_ask_console
  * console_both
    - utter_both_plats
    - utter_ask_talk_anything_else

## happy gaming path 5
  * greet
    - utter_greet
  * mood_feel_good OR affirm
    - utter_happy
    - utter_ask_about_day
  * mood_feel_good OR affirm
    - utter_day_happy
    - utter_ask_talk
  * talk_topic_gaming{"topic": "gaming"}
    - slot{"topic": "gaming"}
    - utter_ask_gaming
  * affirm
    - utter_like_gaming
    - utter_ask_platform
  * platform_console
    - utter_console
    - utter_ask_console
  * console_nintendo
    - utter_nintendo
    - utter_ask_talk_anything_else
  * deny
    - utter_ok
    - utter_goodbye

## happy food path 1
  * greet
   - utter_greet
  * mood_feel_bad
    - utter_feel_bad
    - utter_ask_talk
  * talk_topic_food{"topic": "food"}
    - slot{"topic": "food"}
    - utter_ask_food_1
  * topic_food OR talk_food
    - utter_food_greet
    - utter_ask_food_type
  * type_food_cuisine{"cuisine": "japanese"}
    - slot{"cuisine": "japanese"}
    - utter_greet_cuisine
    - utter_ask_prepare
  * affirm OR deny
    - utter_answer_prepare
    - utter_ask_talk_anything_else
  * affirm
    - utter_ask_talk

## happy food path 2
  * talk_topic_food{"topic": "food"}
    - slot{"topic": "food"}
    - utter_ask_food_1
  * topic_food OR talk_food
    - utter_food_greet
    - utter_ask_food_type
  * type_food_cuisine{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_greet_cuisine
    - utter_ask_prepare
  * affirm OR deny
    - utter_answer_prepare
    - utter_ask_talk_anything_else

## happy food path 3
  * talk_topic_food{"topic": "food"}
    - slot{"topic": "food"}
    - utter_ask_food_1
  * topic_food OR talk_food
    - utter_food_greet
    - utter_ask_food_type
  * type_food_special{"specialty": "pizza"}
    - slot{"specialty": "pizza"}
    - utter_greet_cuisine
    - utter_ask_prepare
  * affirm OR deny
    - utter_answer_prepare
    - utter_ask_talk_anything_else

## happy food path 4
  * greet
   - utter_greet
  * mood_feel_bad
    - utter_feel_bad
    - utter_ask_talk
  * talk_topic_food{"topic": "food"}
    - slot{"topic": "food"}
    - utter_ask_food_1
  * deny
    - utter_food_deny
    - utter_why_food
  * answer_food_deny OR deny
    - utter_react_answer_food_deny
    - utter_ask_talk_anything_else
  * affirm
    - utter_ask_talk

## happy food path 5
  * talk_topic_food{"topic": "food"}
    - slot{"topic": "food"}
    - utter_ask_food_1
  * deny
    - utter_food_deny
    - utter_why_food
  * answer_food_deny OR deny
    - utter_react_answer_food_deny
    - utter_ask_talk_anything_else
  * deny
    - utter_ok
    - utter_goodbye

## happy sports path 1
  * greet
   - utter_greet
  * mood_feel_bad
    - utter_feel_bad
    - utter_ask_talk
  * talk_topic_sports{"topic": "sports"}
    - slot{"topic": "sports"}
    - utter_ask_sports
  * deny_sports OR deny
    - utter_deny_sports
    - utter_why_deny
  * answer_sports_deny OR deny
    - utter_react_answer_sport_deny
    - utter_ask_talk_anything_else

## happy sports path 2
  * talk_topic_sports{"topic": "sports"}
    - slot{"topic": "sports"}
    - utter_ask_sports
  * topic_sports OR affirm
    - utter_affirm_sports
    - utter_favorite_sport
  * type_of_sports{"sport": "golf"}
    - slot{"sport": "golf"}
    - utter_response_sport
    - utter_ask_talk_anything_else

## happy sports path 3
  * talk_topic_sports{"topic": "sports"}
    - slot{"topic": "sports"}
    - utter_ask_sports
  * topic_sports OR affirm
    - utter_affirm_sports
    - utter_favorite_sport
  * type_of_sports{"sport": "soccer"}
    - slot{"sport": "soccer"}
    - utter_response_sport
    - utter_ask_talk_anything_else
  * affirm
    - utter_ask_talk

## movie path 2
  * talk_topic_movies{"topic": "movies"}
    - slot{"topic": "movies"}
    - utter_start_talk_movies
    - utter_fav_movie
    - utter_ask_movie
  * movie_genre_adventure{"genre": "adventure"}
    - slot{"genre": "adventure"}
    - utter_adventure
    - utter_ask_actor
  * movie_actor
    - utter_actor

## movie path 3
  * talk_topic_movies{"topic": "movies"}
    - slot{"topic": "movies"}
    - utter_start_talk_movies
    - utter_fav_movie
    - utter_ask_movie
  * movie_genre_action{"genre": "action"}
    - slot{"genre": "action"}
    - utter_action
    - utter_ask_director
  * movie_director
    - utter_director

## movie path 4
  * talk_topic_movies{"topic": "movies"}
    - slot{"topic": "movies"}
    - utter_start_talk_movies
    - utter_fav_movie
    - utter_ask_movie
  * movie_genre_romantic{"genre": "romantic"}
    - slot{"genre": "romantic"}
    - utter_romantic
    - utter_ask_actor
  * movie_actor
    - utter_actor
    - utter_ask_talk_anything_else
  * deny
    - utter_ok
    - utter_goodbye

## movie path 5
  * talk_topic_movies{"topic": "movies"}
    - slot{"topic": "movies"}
    - utter_start_talk_movies
    - utter_fav_movie
    - utter_ask_movie
  * movie_genre_comedy{"genre": "comedy"}
    - slot{"genre": "comedy"}
    - utter_comedy
    - utter_ask_actor
  * movie_actor
    - utter_actor

## movie path 6
  * talk_topic_movies{"topic": "movies"}
    - slot{"topic": "movies"}
    - utter_start_talk_movies
    - utter_fav_movie
    - utter_ask_movie
  * movie_genre_drama{"genre": "drama"}
    - slot{"genre": "drama"}
    - utter_drama
    - utter_ask_director
  * movie_director
    - utter_director
    - utter_ask_talk_anything_else
  * affirm
    - utter_ask_talk

## change topic 1
  * boring OR change_topic
    - utter_ok
    - utter_ask_talk_anything_else
  * affirm
    - utter_ask_talk

## change topic 2
  * boring OR change_topic
    - utter_ok
    - utter_ask_talk_anything_else
  * deny
    - utter_ok
    - utter_goodbye

## interactive_story_10
  * greet
      - utter_greet
  * mood_feel_bad
      - utter_feel_bad
      - utter_ask_talk
  * talk_topic_food{"topic": "food"}
      - slot{"topic": "food"}
      - utter_ask_food_1
  * topic_food
      - utter_food_greet
      - utter_ask_food_type
  * type_food_cuisine{"cuisine": "chinese"}
      - slot{"cuisine": "chinese"}
      - utter_greet_cuisine
      - utter_ask_prepare
  * deny
      - utter_answer_prepare
      - utter_ask_talk_anything_else
  * affirm
      - utter_ask_talk
  * talk_topic_sports{"topic": "sports"}
      - slot{"topic": "sports"}
      - utter_ask_sports
  * affirm
      - utter_affirm_sports
      - utter_favorite_sport
  * type_of_sports{"sport": "soccer"}
      - slot{"sport": "soccer"}
      - utter_response_sport
      - utter_ask_talk_anything_else
  * deny
      - utter_goodbye

## interactive_story_11
  * greet
      - utter_greet
  * mood_feel_bad
      - utter_feel_bad
      - utter_ask_talk
  * talk_topic_sports{"topic": "sports"}
      - slot{"topic": "sports"}
      - utter_ask_sports
  * affirm
      - utter_affirm_sports
      - utter_favorite_sport
  * type_of_sports{"sport": "basketball"}
      - slot{"sport": "basketball"}
      - utter_response_sport
      - utter_ask_talk_anything_else
  * talk_topic_gaming{"topic": "gaming"}
      - slot{"topic": "gaming"}
      - utter_ask_gaming
  * affirm
      - utter_like_gaming
      - utter_ask_platform
  * console_both
      - utter_both_plats
      - utter_ask_talk_anything_else
  * deny
      - utter_ok
      - utter_goodbye

## interactive_story_12
  * talk_topic_food{"topic": "food"}
      - slot{"topic": "food"}
      - utter_ask_food_1
  * topic_food
      - utter_food_greet
      - utter_ask_food_type
  * type_food_special{"specialty": "pizza"}
      - slot{"specialty": "pizza"}
      - utter_greet_cuisine
      - utter_ask_prepare
  * deny
      - utter_answer_prepare
      - utter_ask_talk_anything_else
  * deny
      - utter_ok
      - utter_goodbye
  * goodbye
      - utter_goodbye

## interactive_story_13
  * greet
      - utter_greet
  * mood_feel_bad
      - utter_feel_bad
      - utter_ask_talk
  * talk_topic_movies{"topic": "movies"}
      - slot{"topic": "movies"}
      - utter_start_talk_movies
      - utter_fav_movie
      - utter_ask_movie

## interactive_story_14
  * greet
      - utter_greet
  * mood_feel_bad
      - utter_feel_bad
      - utter_ask_talk
  * talk_topic_sports{"topic": "sports"}
      - slot{"topic": "sports"}
      - utter_ask_sports
  * affirm{"topic": "sports"}
      - slot{"topic": "sports"}
      - utter_affirm_sports
      - utter_favorite_sport
  * type_of_sports{"sport": "basketball"}
      - slot{"sport": "basketball"}
      - utter_response_sport
      - utter_ask_talk_anything_else
  * affirm
      - utter_ask_talk
  * talk_topic_movies{"topic": "movies", "genre": "romantic"}
      - slot{"genre": "romantic"}
      - slot{"topic": "movies"}
      - utter_romantic
      - utter_ask_actor
  * movie_actor{"actor": "Ryan Gosling"}
      - utter_actor
  * goodbye
      - utter_goodbye

<!-- ## path action test
  * need_advice
    - action_image -->

<!-- ## go to sports
* affirm{"topic": "sports"}
  - utter_affirm_sports

## go to sports
* affirm{"topic": "movies"}
  - utter_start_talk_movies

## go to sports
* affirm{"topic": "food"}
  - utter_ask_food_1

## go to sports
* affirm{"topic": "gaming"}
  - utter_ask_gaming -->

## path recommendation 1
  * recommendation{"content_type": "image"}
    - slot{"content_type": "image"}
    - action_recommend

## path recommendation 2
  * talk_topic_gaming{"topic": "gaming"}
      - slot{"topic": "gaming"}
      - utter_ask_gaming
  * affirm
      - utter_like_gaming
      - utter_ask_platform
  * recommendation{"content_type": "video"}
    - slot{"content_type": "video"}
    - action_recommend
<!--
  * platform_console
    - utter_console
    - utter_ask_console
  * console_nintendo
    - utter_nintendo
    - utter_ask_talk_anything_else -->
