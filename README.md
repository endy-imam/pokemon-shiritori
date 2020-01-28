# Pokémon Shiritori (ポケモンしりとり)

A visualized data structure of a Japanese children's word game called 'Shiritori', but with Pokémon.


## Background

**'Shiritori'** - literally "taking the end" - is a game where players are required to say a noun that ends with the final kana (Japanese character) of a previous word. If the player said a word that ends with an N-kana (ん/ン), they lose.

For example:

| JPN Kana    | Romaji        | English |
| -----------:| -------------:| ------- |
| さく**ら**   | _saku_**RA**  | sakura  |
| ラジ**オ**   | _raji_**O**   | radio   |
| おにぎ**り** | _onigi_**RI** | onigiri |
| すも**う**   | _sumo_**U**   | sumo    |
| うど**ん**   | _udo_**N**    | udon    |

The player saying _udon_ lose this game.

There can optional rules that can be added but for this case, some strict rules are enforced:

- **Dakuten (ﾞ)** and **Handakuten (ﾟ)** kanas are enforced (ex. _Ha (は)_, _Ba (ば)_, and _Pa (ぱ)_ are separate).
- **Long Vowel Sounds (ー)** should be ignored (ex. ウールー (Uuruu / Wooloo) would assume to end as _Ru (る)_ and not _U (ウ)_ by the vowel extension).

Down the line, those rules could be toggleable by an option.

### How Pokémon Fit Into This?

At least in Japanese (the home of Pokémon), it's a fun way of test the amount of Pokémon you know by name and there's videos and music that plays through a game of Pokémon Shiritori where the words are limited to (Japanese) Pokémon Names:

- https://www.youtube.com/watch?v=5cYH53TgGQI
- https://www.youtube.com/watch?v=4yXzri9CTTM
- https://www.youtube.com/watch?v=RlSff8PjoGs
