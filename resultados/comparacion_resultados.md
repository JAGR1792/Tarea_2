# Resultados de Comparacion CYK vs ANTLR4

| Entrada | Tokens | CYK | ANTLR4 | Tiempo CYK (s) | Tiempo ANTLR4 (s) |
|---|---:|---|---|---:|---:|
| a b bas | 3 | ACEPTADA | ACEPTADA | 0.00004323 | 0.00111023 |
| a b bas c | 4 | ACEPTADA | ACEPTADA | 0.00003026 | 0.00027316 |
| a big boss | 3 | ACEPTADA | ACEPTADA | 0.00001545 | 0.00029374 |
| a big c boss | 4 | ACEPTADA | ACEPTADA | 0.00001894 | 0.00021105 |
| a big boss c | 4 | ACEPTADA | ACEPTADA | 0.00003338 | 0.00021448 |
| a big c boss c | 5 | ACEPTADA | ACEPTADA | 0.00003288 | 0.00020225 |
| a bas | 2 | RECHAZADA | RECHAZADA | 0.00001016 | 0.00029170 |
| big c boss | 3 | RECHAZADA | RECHAZADA | 0.00001463 | 0.00027179 |
| a b bas c c c | 6 | RECHAZADA | RECHAZADA | 0.00005430 | 0.00028222 |
| a b bas c c c c | 7 | RECHAZADA | RECHAZADA | 0.00004851 | 0.00028395 |
| a b bas c c c c c | 8 | RECHAZADA | RECHAZADA | 0.00006879 | 0.00030104 |
| a big c boss c c c | 7 | RECHAZADA | RECHAZADA | 0.00005311 | 0.00028142 |
| a big c boss c c c c | 8 | RECHAZADA | RECHAZADA | 0.00006477 | 0.00028536 |
| a big c boss c c c c c | 9 | RECHAZADA | RECHAZADA | 0.00008651 | 0.00033176 |
| a b bas c c c c c c c c | 11 | RECHAZADA | RECHAZADA | 0.00011929 | 0.00032317 |
| a b bas c c c c c c c c c c | 13 | RECHAZADA | RECHAZADA | 0.00013192 | 0.00037615 |
| a big c boss c c c c c c c c | 12 | RECHAZADA | RECHAZADA | 0.00011179 | 0.00039826 |
| a big c boss c c c c c c c c c c | 14 | RECHAZADA | RECHAZADA | 0.00017482 | 0.00048171 |
| a b bas c c c c c c c c c c c c c c | 17 | RECHAZADA | RECHAZADA | 0.00023353 | 0.00048544 |
| a b bas c c c c c c c c c c c c c c c c | 19 | RECHAZADA | RECHAZADA | 0.00029289 | 0.00046083 |
| a big c boss c c c c c c c c c c c c c c | 18 | RECHAZADA | RECHAZADA | 0.00027304 | 0.00044780 |
| a big c boss c c c c c c c c c c c c c c c c | 20 | RECHAZADA | RECHAZADA | 0.00034462 | 0.00047456 |
| a b bas c c c c c c c c c c c c c c c c c c c c c | 24 | RECHAZADA | RECHAZADA | 0.00051567 | 0.00051861 |
| a b bas c c c c c c c c c c c c c c c c c c c c c c c | 26 | RECHAZADA | RECHAZADA | 0.00070894 | 0.00063385 |
| a big c boss c c c c c c c c c c c c c c c c c c c c c | 25 | RECHAZADA | RECHAZADA | 0.00054025 | 0.00067582 |
| a big c boss c c c c c c c c c c c c c c c c c c c c c c c | 27 | RECHAZADA | RECHAZADA | 0.00083364 | 0.00103687 |
| a b bas c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 31 | RECHAZADA | RECHAZADA | 0.00116526 | 0.00083181 |
| a b bas c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 33 | RECHAZADA | RECHAZADA | 0.00109263 | 0.00083351 |
| a big c boss c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 32 | RECHAZADA | RECHAZADA | 0.00092995 | 0.00069231 |
| a big c boss c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 34 | RECHAZADA | RECHAZADA | 0.00112475 | 0.00072265 |
| a b bas c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 38 | RECHAZADA | RECHAZADA | 0.00152210 | 0.00091236 |
| a b bas c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 39 | RECHAZADA | RECHAZADA | 0.00168984 | 0.00092914 |
| a big c boss c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 38 | RECHAZADA | RECHAZADA | 0.00149986 | 0.00107254 |
| a big c boss c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 40 | RECHAZADA | RECHAZADA | 0.00182009 | 0.00102236 |
| a b bas c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 45 | RECHAZADA | RECHAZADA | 0.00235326 | 0.00108950 |
| a b bas c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 46 | RECHAZADA | RECHAZADA | 0.00440529 | 0.00107273 |
| a big c boss c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 45 | RECHAZADA | RECHAZADA | 0.00233891 | 0.00102746 |
| a big c boss c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 46 | RECHAZADA | RECHAZADA | 0.00277437 | 0.00117051 |
| a b bas c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 50 | RECHAZADA | RECHAZADA | 0.00304504 | 0.00109301 |
| a b bas c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 52 | RECHAZADA | RECHAZADA | 0.00364470 | 0.00112266 |
| a big c boss c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 51 | RECHAZADA | RECHAZADA | 0.00339175 | 0.00120655 |
| a big c boss c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 53 | RECHAZADA | RECHAZADA | 0.00394098 | 0.00123519 |
| a b bas c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 58 | RECHAZADA | RECHAZADA | 0.00447055 | 0.00120077 |
| a b bas c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 59 | RECHAZADA | RECHAZADA | 0.00545329 | 0.00173403 |
| a big c boss c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 58 | RECHAZADA | RECHAZADA | 0.00444179 | 0.00109174 |
| a big c boss c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 59 | RECHAZADA | RECHAZADA | 0.00458307 | 0.00127176 |
| a b bas c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 64 | RECHAZADA | RECHAZADA | 0.00705920 | 0.00135418 |
| a b bas c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 65 | RECHAZADA | RECHAZADA | 0.00598785 | 0.00121836 |
| a big c boss c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 64 | RECHAZADA | RECHAZADA | 0.00564651 | 0.00127074 |
| a big c boss c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c | 65 | RECHAZADA | RECHAZADA | 0.00496176 | 0.00107219 |
| a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas | 117 | RECHAZADA | RECHAZADA | 0.02403111 | 0.00146854 |
| a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas | 120 | RECHAZADA | RECHAZADA | 0.02130940 | 0.00102963 |
| a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas | 123 | RECHAZADA | RECHAZADA | 0.02122732 | 0.00103380 |
| a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas | 126 | RECHAZADA | RECHAZADA | 0.02347787 | 0.00112780 |
| a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas | 129 | RECHAZADA | RECHAZADA | 0.02529113 | 0.00107038 |
| a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas | 132 | RECHAZADA | RECHAZADA | 0.02634731 | 0.00121527 |
| a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas | 135 | RECHAZADA | RECHAZADA | 0.02792633 | 0.00113997 |
| a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas | 138 | RECHAZADA | RECHAZADA | 0.03004061 | 0.00128134 |
| a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas | 141 | RECHAZADA | RECHAZADA | 0.03246940 | 0.00136857 |
| a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas | 144 | RECHAZADA | RECHAZADA | 0.03370667 | 0.00123927 |
| a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas | 147 | RECHAZADA | RECHAZADA | 0.04574861 | 0.00123323 |
| a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas a b bas | 150 | RECHAZADA | RECHAZADA | 0.03894856 | 0.00129793 |
