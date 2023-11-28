# Pagat scraper

A quick script that scrapes Pagat for traditional card games and combines it with the boardgamegeek rankings from https://www.kaggle.com/datasets/threnjen/board-games-database-from-boardgamegeek/code
(It requires games.csv from the above link.)

## Results

| name                                                                         | players          | design              | quantity                                       |   bgg_ranking |   gameweight |   ranking |
|:-----------------------------------------------------------------------------|:-----------------|:--------------------|:-----------------------------------------------|--------------:|-------------:|----------:|
| [Sheepshead](https://www.pagat.com/schafkopf/shep.html)                      | 3–5              | French suited cards | 32                                             |       8.18636 |       3      |      6381 |
| [Ulti](https://www.pagat.com/marriage/ulti.html)                             | 3, 4             | German suited cards | 32                                             |       8.08627 |       3.3333 |      9609 |
| [Mus](https://www.pagat.com/vying/mus.html)                                  | 4                | Latin suited cards  | 40                                             |       7.92928 |       2.2692 |      2581 |
| [Cuttle](https://www.pagat.com/combat/cuttle.html)                           | 2                | French suited cards | 52                                             |       7.65875 |       2.4    |     13715 |
| [Preference](https://www.pagat.com/preference/)                              |                  |                     |                                                |       7.57075 |       3.3125 |      8255 |
| [Doppelkopf](https://www.pagat.com/schafkopf/doko.html)                      | 4, 5             | French suited cards | 2x20, 2x24                                     |       7.52927 |       2.9429 |      2164 |
| [Bridge](https://www.pagat.com/auctionwhist/bridge.html)                     | 4                | French suited cards | 52                                             |       7.45542 |       3.8562 |       771 |
| [Briscola Chiamata](https://www.pagat.com/aceten/briscola_chiamata.html)     | 5–7              | French suited cards | 40                                             |       7.43423 |       2      |      8359 |
| [Eleusis](https://www.pagat.com/eights/eleusis.html)                         | 3, 4–7           | French suited cards | 3x52, 4x52                                     |       7.39634 |       2.9333 |      5190 |
| [Truco](https://www.pagat.com/put/truco.html)                                |                  |                     |                                                |       7.26807 |       1.9286 |      6690 |
| [Skat](https://www.pagat.com/schafkopf/skat.html)                            | 3, 4             | German suited cards | 32                                             |       7.23688 |       3.0561 |      1983 |
| [Bid Euchre](https://www.pagat.com/euchre/bideuch.html)                      | 3, 4, 6, 8       | French suited cards | 24, 2x16, 2x20, 2x24                           |       7.23243 |       1.6667 |     12186 |
| [Trains](https://www.pagat.com/domino/disconnected/trains.html)              | 4–10             | Western dominoes    | 55, 91                                         |       7.15583 |       2.3881 |       540 |
| [Machiavelli](https://www.pagat.com/rummy/carousel.html#machiavelli)         | 2–5              | French suited cards | 2x52                                           |       7.0996  |       3.2075 |      2239 |
| [Watten](https://www.pagat.com/trumps/watten.html)                           | 2, 3, 4          | German suited cards | 32, 33, 36                                     |       7.0783  |       2.125  |     10434 |
| [Kaiser](https://www.pagat.com/pointtrk/kaiser.html)                         | 2, 3, 4, 6       | French suited cards | 26, 32, 34, 48                                 |       7.07    |       1.8    |     12388 |
| [Cribbage](https://www.pagat.com/adders/crib6.html)                          |                  |                     |                                                |       7.06471 |       1.9029 |       641 |
| [Klaverjassen](https://www.pagat.com/jass/klaverjassen.html)                 | 4                | French suited cards | 32                                             |       7.0248  |       2.8125 |      7292 |
| [Schnapsen](https://www.pagat.com/marriage/schnaps.html)                     | 2                | German suited cards | 20                                             |       7.02256 |       2.037  |      5113 |
| [King](https://www.pagat.com/compendium/king.html)                           | 4                | French suited cards | 52                                             |       6.96939 |       2      |      9872 |
| [500](https://www.pagat.com/euchre/500.html)                                 | 2, 3, 4, 5, 6    | French suited cards | 32+J, 42+J, 44+J, 44+2J, 52+J, 62+J            |       6.96547 |       2.04   |      3766 |
| [Calypso](https://www.pagat.com/pointtrk/calypso.html)                       | 4                | French suited cards | 4x52                                           |       6.90566 |       2.4    |     11348 |
| [Pinochle](https://www.pagat.com/marriage/pinmain.html)                      |                  |                     |                                                |       6.86701 |       2.2989 |      2589 |
| [Oh Hell!](https://www.pagat.com/exact/ohhell.html)                          | 3, 4–6, 7        | French suited cards | 52                                             |       6.84374 |       1.7315 |      2206 |
| [Euchre](https://www.pagat.com/euchre/euchre.html)                           | 4, 6             | French suited cards | 24, 24+J, 32, 32+J, 2x24+2J                    |       6.80866 |       1.7025 |      1691 |
| [Tute](https://www.pagat.com/marriage/tute.html)                             | 4                | Latin suited cards  | 40                                             |       6.80816 |       2      |     11628 |
| [Barbu](https://www.pagat.com/compendium/barbu.html)                         | 4                | French suited cards | 52                                             |       6.78804 |       2.2857 |      8138 |
| [Pitch](https://www.pagat.com/allfours/pitch.html)                           | 2, 3–6, 7        | French suited cards | 52                                             |       6.76627 |       1.7727 |      5628 |
| [Spades](https://www.pagat.com/auctionwhist/spades.html)                     | 2, 3, 4, 6       | French suited cards | 52, 52+2J, 2x51                                |       6.76555 |       2.0349 |      1793 |
| [Poker](https://www.pagat.com/poker/)                                        |                  |                     |                                                |       6.71893 |       2.4451 |      1089 |
| [Speculation](https://www.pagat.com/misc/speculation.html)                   | 3–8              | French suited cards | 52                                             |       6.68647 |       2      |      3214 |
| [Klabberjass](https://www.pagat.com/jass/klabberjass.html)                   | 2, 3, 4          | French suited cards | 32                                             |       6.6619  |       2.75   |     14138 |
| [Big Two](https://www.pagat.com/climbing/bigtwo.html)                        | 2, 3, 4          | French suited cards | 52                                             |       6.66017 |       1.7353 |      5652 |
| [Go Stop](https://www.pagat.com/fishing/gostop.html)                         | 2–7              | Flower cards        | 48+5J                                          |       6.63423 |       2.1667 |      7146 |
| [Belote](https://www.pagat.com/jass/belote.html)                             | 4                | French suited cards | 32                                             |       6.61692 |       2.625  |      6409 |
| [Scopa](https://www.pagat.com/fishing/scopa.html)                            | 2, 3, 4, 6       | French suited cards | 40                                             |       6.58389 |       1.4928 |      3379 |
| [Mate](https://www.pagat.com/misc/mate.html)                                 | 2                | French suited cards | 20                                             |       6.58143 |       2.375  |     11943 |
| [Bluff](https://www.pagat.com/beating/doubt.html#bluff)                      | 3–6              | French suited cards | 52                                             |       6.56096 |       0      |      8364 |
| [Hungarian Tarokk](https://www.pagat.com/tarot/xx-hivas.html)                | 4, 5             | French suited Tarot | 42                                             |       6.54878 |       3.5    |     14260 |
| [Pyramid Poker](https://www.pagat.com/poker/variants/ironcross.html#pyramid) | 3, 4, 5–8, 9     | French suited cards | 52                                             |       6.5057  |       1.3    |      3897 |
| [Piquet](https://www.pagat.com/notrump/piquet.html)                          | 2                | French suited cards | 32                                             |       6.49728 |       2.5    |     10845 |
| [German Whist](https://www.pagat.com/whist/german_whist.html)                | 2                | French suited cards | 52                                             |       6.49247 |       1.8889 |     10057 |
| [Bezique](https://www.pagat.com/marriage/bezique.html)                       | 2                | French suited cards | 2x32                                           |       6.49048 |       2.3333 |     10656 |
| [1000](https://www.pagat.com/marriage/1000.html)                             | 3, 4             | French suited cards | 24                                             |       6.47619 |       1.8    |     14640 |
| [Hearts](https://www.pagat.com/reverse/hearts.html)                          | 3, 4, 5          | French suited cards | 52                                             |       6.45961 |       1.7649 |      1891 |
| [Tahiti](https://www.pagat.com/rummy/carousel.html#tahiti)                   | 2–5              | French suited cards | 2x52+4J                                        |       6.44262 |       2.1667 |     12387 |
| [Contract Rummy](https://www.pagat.com/rummy/ctrummy.html)                   | 3–5              | French suited cards | 2x52+2J, 2x52+3J, 2x52+4J, 3x52+6J             |       6.42933 |       1.8462 |      8400 |
| [Écarté](https://www.pagat.com/trumps/ecarte.html)                           | 2                | French suited cards | 32                                             |       6.42209 |       2.125  |     14533 |
| [Durak](https://www.pagat.com/beating/durak.html)                            |                  |                     |                                                |       6.38569 |       1.5263 |      6917 |
| [Canasta](https://www.pagat.com/rummy/canasta.html)                          | 2, 3, 4          | French suited cards | 2x52+4J                                        |       6.38478 |       2.1275 |      3444 |
| [Okey](https://www.pagat.com/rummy/okey.html)                                | 4                | Number tiles        | 2x52+2J                                        |       6.3617  |       1.5714 |     14254 |
| [Briscola](https://www.pagat.com/aceten/briscola.html)                       | 2–6              | French suited cards | 32, 36, 39, 40                                 |       6.35394 |       1.5405 |      5615 |
| [Pegs and Jokers](https://www.pagat.com/race/pegsandjokers.html)             | 4, 6, 8          | French suited cards | 3x52+6J, 4x52+8J                               |       6.35258 |       1.5    |     12121 |
| [Gin Rummy](https://www.pagat.com/rummy/ginrummy.html)                       | 2, 3, 4          | French suited cards | 52, 2x52                                       |       6.30525 |       1.6966 |      3589 |
| [Sueca](https://www.pagat.com/aceten/sueca.html)                             | 4                | French suited cards | 40                                             |       6.29403 |       2      |     15814 |
| [Casino](https://www.pagat.com/fishing/casino.html)                          | 2, 3, 4          | French suited cards | 52                                             |       6.29366 |       1.4    |      6873 |
| [Charlemagne](https://www.pagat.com/euchre/charlemagne.html)                 | 4                | French suited cards | 32, 32+2J                                      |       6.27667 |       4      |     15685 |
| [Russian Bank](https://www.pagat.com/patience/crapette.html)                 | 2                | French suited cards | 2x52                                           |       6.05    |       1.3333 |     16256 |
| [Chinese Poker](https://www.pagat.com/partition/pusoy.html)                  | 2, 3, 4          | French suited cards | 52                                             |       6.02667 |       2      |     14925 |
| [Pepper](https://www.pagat.com/euchre/pepper.html)                           | 2, 3, 4          | French suited cards | 24                                             |       6.00582 |       1.7778 |     11083 |
| [Kemps](https://www.pagat.com/commerce/kemps.html)                           | 4, 6, 8          | French suited cards | 52                                             |       5.93317 |       1.1667 |     14762 |
| [Chicago Poker](https://www.pagat.com/poker/variants/chicago.html#high)      | 2–4, 5–7, 8      | French suited cards | 52                                             |       5.88899 |       1.7455 |      7567 |
| [Hand and Foot](https://www.pagat.com/rummy/handfoot.html)                   | 2, 3, 4–6        | French suited cards | 3x52+6J, 4x52+8J, 5x52+10J, 6x52+12J, 7x52+14J |       5.88739 |       1.92   |     10212 |
| [Yaniv](https://www.pagat.com/draw/yaniv.html)                               | 2–5, 6–8         | French suited cards | 52, 52+2J                                      |       5.8422  |       1.4    |     15667 |
| [Bourré](https://www.pagat.com/rams/boure.html)                              | 2–5, 6–8         | French suited cards | 52                                             |       5.82979 |       1.6667 |     16877 |
| [Mexican Train](https://www.pagat.com/domino/star/mextrain.html)             | 2, 3, 4–8, 9, 10 | Western dominoes    | 55, 91                                         |       5.7139  |       1.2662 |      8115 |
| [Mao](https://www.pagat.com/eights/mao.html)                                 | 2, 3–8, 9–12     | French suited cards | 52, 2x52, 3x52                                 |       5.65534 |       2      |     15509 |
| [Egyptian Ratscrew](https://www.pagat.com/war/egyptrat.html)                 | 2–7              | French suited cards | 52                                             |       5.59932 |       1.2381 |     16763 |
| [GOPS](https://www.pagat.com/misc/gops.html)                                 | 2, 3             | French suited cards | 39, 52                                         |       5.55556 |       1.625  |     17558 |
| [Speed](https://www.pagat.com/patience/spit.html#speed)                      | 2                | French suited cards | 52                                             |       5.44844 |       1.1111 |     18422 |
| [Golf](https://www.pagat.com/draw/golf.html)                                 | 2–8              | French suited cards | 52, 2x52                                       |       5.43598 |       1.36   |     19961 |
| [Fan Tan](https://www.pagat.com/layout/sevens.html)                          | 3, 4–6, 7, 8     | French suited cards | 52                                             |       5.42169 |       1.3    |     19039 |
| [Conquian](https://www.pagat.com/rummy/conquian.html)                        | 2                | French suited cards | 40                                             |       5.39677 |       2      |     18201 |
| [Smear](https://www.pagat.com/allfours/schmier.html)                         | 2–6              | French suited cards | 32, 32+2J, 40, 44+J, 52, 52+J, 52+2J           |       5.37856 |       1.1667 |     18435 |
| [Shanghai](https://www.pagat.com/rummy/carousel.html#shanghai)               | 3, 4, 5          | French suited cards | 2x52                                           |       5.33028 |       1.7    |     19686 |
| [Dingo](https://www.pagat.com/misc/dingo.html)                               | 4                | French suited cards | 52                                             |       4.98627 |       1      |     19864 |
| [Happy Families](https://www.pagat.com/quartet/gofish.html#families)         | 3–6              | French suited cards | 44, 52                                         |       4.769   |       1.0556 |     21462 |
| [Quartett](https://www.pagat.com/quartet/gofish.html#quartet)                | 3–6              | French suited cards | 32                                             |       4.40598 |       1      |     21297 |
| [Crazy Eights](https://www.pagat.com/eights/crazy8s.html)                    | 2–8              | French suited cards | 52, 2x52                                       |       4.39646 |       1.0714 |     21642 |
| [Top Trumps](https://www.pagat.com/com/top_trumps.html)                      | 2–4, 5, 6        | Top Trumps cards    | 48                                             |       4.23094 |       1.0526 |     21652 |
| [Old Maid](https://www.pagat.com/passing/oldmaid.html)                       | 2, 3–8, 9, 10    | French suited cards | 43, 51                                         |       3.64365 |       1.0496 |     21672 |
| [Go Fish](https://www.pagat.com/quartet/gofish.html)                         | 2, 3–6           | French suited cards | 52                                             |       3.63529 |       1.0614 |     21674 |
| [Snap](https://www.pagat.com/war/snap.html)                                  | 2–6              | French suited cards | 52                                             |       3.43597 |       1.1429 |     21604 |
| [War](https://www.pagat.com/war/war.html)                                    | 2, 3, 4          | French suited cards | 52, 52+2J                                      |       2.29913 |       1      |     21680 |