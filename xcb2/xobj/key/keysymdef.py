#!/usr/bin/env python
# -*- coding: utf-8 -*-

r"""keysymdef -- DESCRIPTION

"""
from pprint import pformat as _pformat

from t1.dictutil import swapdict as _swapdict
from xcb2 import NoSymbol

import keysym
import namesym
import err


LEGACY = {
    0x01A1: 0x0104,
    0x01A2: 0x02D8,
    0x01A3: 0x0141,
    0x01A5: 0x013D,
    0x01A6: 0x015A,
    0x01A9: 0x0160,
    0x01AA: 0x015E,
    0x01AB: 0x0164,
    0x01AC: 0x0179,
    0x01AE: 0x017D,
    0x01AF: 0x017B,
    0x01B1: 0x0105,
    0x01B2: 0x02DB,
    0x01B3: 0x0142,
    0x01B5: 0x013E,
    0x01B6: 0x015B,
    0x01B7: 0x02C7,
    0x01B9: 0x0161,
    0x01BA: 0x015F,
    0x01BB: 0x0165,
    0x01BC: 0x017A,
    0x01BD: 0x02DD,
    0x01BE: 0x017E,
    0x01BF: 0x017C,
    0x01C0: 0x0154,
    0x01C3: 0x0102,
    0x01C5: 0x0139,
    0x01C6: 0x0106,
    0x01C8: 0x010C,
    0x01CA: 0x0118,
    0x01CC: 0x011A,
    0x01CF: 0x010E,
    0x01D0: 0x0110,
    0x01D1: 0x0143,
    0x01D2: 0x0147,
    0x01D5: 0x0150,
    0x01D8: 0x0158,
    0x01D9: 0x016E,
    0x01DB: 0x0170,
    0x01DE: 0x0162,
    0x01E0: 0x0155,
    0x01E3: 0x0103,
    0x01E5: 0x013A,
    0x01E6: 0x0107,
    0x01E8: 0x010D,
    0x01EA: 0x0119,
    0x01EC: 0x011B,
    0x01EF: 0x010F,
    0x01F0: 0x0111,
    0x01F1: 0x0144,
    0x01F2: 0x0148,
    0x01F5: 0x0151,
    0x01F8: 0x0159,
    0x01F9: 0x016F,
    0x01FB: 0x0171,
    0x01FE: 0x0163,
    0x01FF: 0x02D9,
    0x02A1: 0x0126,
    0x02A6: 0x0124,
    0x02A9: 0x0130,
    0x02AB: 0x011E,
    0x02AC: 0x0134,
    0x02B1: 0x0127,
    0x02B6: 0x0125,
    0x02B9: 0x0131,
    0x02BB: 0x011F,
    0x02BC: 0x0135,
    0x02C5: 0x010A,
    0x02C6: 0x0108,
    0x02D5: 0x0120,
    0x02D8: 0x011C,
    0x02DD: 0x016C,
    0x02DE: 0x015C,
    0x02E5: 0x010B,
    0x02E6: 0x0109,
    0x02F5: 0x0121,
    0x02F8: 0x011D,
    0x02FD: 0x016D,
    0x02FE: 0x015D,
    0x03A2: 0x0138,
    0x03A3: 0x0156,
    0x03A5: 0x0128,
    0x03A6: 0x013B,
    0x03AA: 0x0112,
    0x03AB: 0x0122,
    0x03AC: 0x0166,
    0x03B3: 0x0157,
    0x03B5: 0x0129,
    0x03B6: 0x013C,
    0x03BA: 0x0113,
    0x03BB: 0x0123,
    0x03BC: 0x0167,
    0x03BD: 0x014A,
    0x03BF: 0x014B,
    0x03C0: 0x0100,
    0x03C7: 0x012E,
    0x03CC: 0x0116,
    0x03CF: 0x012A,
    0x03D1: 0x0145,
    0x03D2: 0x014C,
    0x03D3: 0x0136,
    0x03D9: 0x0172,
    0x03DD: 0x0168,
    0x03DE: 0x016A,
    0x03E0: 0x0101,
    0x03E7: 0x012F,
    0x03EC: 0x0117,
    0x03EF: 0x012B,
    0x03F1: 0x0146,
    0x03F2: 0x014D,
    0x03F3: 0x0137,
    0x03F9: 0x0173,
    0x03FD: 0x0169,
    0x03FE: 0x016B,
    0x047E: 0x203E,
    0x04A1: 0x3002,
    0x04A2: 0x300C,
    0x04A3: 0x300D,
    0x04A4: 0x3001,
    0x04A5: 0x30FB,
    0x04A6: 0x30F2,
    0x04A7: 0x30A1,
    0x04A8: 0x30A3,
    0x04A9: 0x30A5,
    0x04AA: 0x30A7,
    0x04AB: 0x30A9,
    0x04AC: 0x30E3,
    0x04AD: 0x30E5,
    0x04AE: 0x30E7,
    0x04AF: 0x30C3,
    0x04B0: 0x30FC,
    0x04B1: 0x30A2,
    0x04B2: 0x30A4,
    0x04B3: 0x30A6,
    0x04B4: 0x30A8,
    0x04B5: 0x30AA,
    0x04B6: 0x30AB,
    0x04B7: 0x30AD,
    0x04B8: 0x30AF,
    0x04B9: 0x30B1,
    0x04BA: 0x30B3,
    0x04BB: 0x30B5,
    0x04BC: 0x30B7,
    0x04BD: 0x30B9,
    0x04BE: 0x30BB,
    0x04BF: 0x30BD,
    0x04C0: 0x30BF,
    0x04C1: 0x30C1,
    0x04C2: 0x30C4,
    0x04C3: 0x30C6,
    0x04C4: 0x30C8,
    0x04C5: 0x30CA,
    0x04C6: 0x30CB,
    0x04C7: 0x30CC,
    0x04C8: 0x30CD,
    0x04C9: 0x30CE,
    0x04CA: 0x30CF,
    0x04CB: 0x30D2,
    0x04CC: 0x30D5,
    0x04CD: 0x30D8,
    0x04CE: 0x30DB,
    0x04CF: 0x30DE,
    0x04D0: 0x30DF,
    0x04D1: 0x30E0,
    0x04D2: 0x30E1,
    0x04D3: 0x30E2,
    0x04D4: 0x30E4,
    0x04D5: 0x30E6,
    0x04D6: 0x30E8,
    0x04D7: 0x30E9,
    0x04D8: 0x30EA,
    0x04D9: 0x30EB,
    0x04DA: 0x30EC,
    0x04DB: 0x30ED,
    0x04DC: 0x30EF,
    0x04DD: 0x30F3,
    0x04DE: 0x309B,
    0x04DF: 0x309C,
    0x05AC: 0x060C,
    0x05BB: 0x061B,
    0x05BF: 0x061F,
    0x05C1: 0x0621,
    0x05C2: 0x0622,
    0x05C3: 0x0623,
    0x05C4: 0x0624,
    0x05C5: 0x0625,
    0x05C6: 0x0626,
    0x05C7: 0x0627,
    0x05C8: 0x0628,
    0x05C9: 0x0629,
    0x05CA: 0x062A,
    0x05CB: 0x062B,
    0x05CC: 0x062C,
    0x05CD: 0x062D,
    0x05CE: 0x062E,
    0x05CF: 0x062F,
    0x05D0: 0x0630,
    0x05D1: 0x0631,
    0x05D2: 0x0632,
    0x05D3: 0x0633,
    0x05D4: 0x0634,
    0x05D5: 0x0635,
    0x05D6: 0x0636,
    0x05D7: 0x0637,
    0x05D8: 0x0638,
    0x05D9: 0x0639,
    0x05DA: 0x063A,
    0x05E0: 0x0640,
    0x05E1: 0x0641,
    0x05E2: 0x0642,
    0x05E3: 0x0643,
    0x05E4: 0x0644,
    0x05E5: 0x0645,
    0x05E6: 0x0646,
    0x05E7: 0x0647,
    0x05E8: 0x0648,
    0x05E9: 0x0649,
    0x05EA: 0x064A,
    0x05EB: 0x064B,
    0x05EC: 0x064C,
    0x05ED: 0x064D,
    0x05EE: 0x064E,
    0x05EF: 0x064F,
    0x05F0: 0x0650,
    0x05F1: 0x0651,
    0x05F2: 0x0652,
    0x06A1: 0x0452,
    0x06A2: 0x0453,
    0x06A3: 0x0451,
    0x06A4: 0x0454,
    0x06A5: 0x0455,
    0x06A6: 0x0456,
    0x06A7: 0x0457,
    0x06A8: 0x0458,
    0x06A9: 0x0459,
    0x06AA: 0x045A,
    0x06AB: 0x045B,
    0x06AC: 0x045C,
    0x06AD: 0x0491,
    0x06AE: 0x045E,
    0x06AF: 0x045F,
    0x06B0: 0x2116,
    0x06B1: 0x0402,
    0x06B2: 0x0403,
    0x06B3: 0x0401,
    0x06B4: 0x0404,
    0x06B5: 0x0405,
    0x06B6: 0x0406,
    0x06B7: 0x0407,
    0x06B8: 0x0408,
    0x06B9: 0x0409,
    0x06BA: 0x040A,
    0x06BB: 0x040B,
    0x06BC: 0x040C,
    0x06BD: 0x0490,
    0x06BE: 0x040E,
    0x06BF: 0x040F,
    0x06C0: 0x044E,
    0x06C1: 0x0430,
    0x06C2: 0x0431,
    0x06C3: 0x0446,
    0x06C4: 0x0434,
    0x06C5: 0x0435,
    0x06C6: 0x0444,
    0x06C7: 0x0433,
    0x06C8: 0x0445,
    0x06C9: 0x0438,
    0x06CA: 0x0439,
    0x06CB: 0x043A,
    0x06CC: 0x043B,
    0x06CD: 0x043C,
    0x06CE: 0x043D,
    0x06CF: 0x043E,
    0x06D0: 0x043F,
    0x06D1: 0x044F,
    0x06D2: 0x0440,
    0x06D3: 0x0441,
    0x06D4: 0x0442,
    0x06D5: 0x0443,
    0x06D6: 0x0436,
    0x06D7: 0x0432,
    0x06D8: 0x044C,
    0x06D9: 0x044B,
    0x06DA: 0x0437,
    0x06DB: 0x0448,
    0x06DC: 0x044D,
    0x06DD: 0x0449,
    0x06DE: 0x0447,
    0x06DF: 0x044A,
    0x06E0: 0x042E,
    0x06E1: 0x0410,
    0x06E2: 0x0411,
    0x06E3: 0x0426,
    0x06E4: 0x0414,
    0x06E5: 0x0415,
    0x06E6: 0x0424,
    0x06E7: 0x0413,
    0x06E8: 0x0425,
    0x06E9: 0x0418,
    0x06EA: 0x0419,
    0x06EB: 0x041A,
    0x06EC: 0x041B,
    0x06ED: 0x041C,
    0x06EE: 0x041D,
    0x06EF: 0x041E,
    0x06F0: 0x041F,
    0x06F1: 0x042F,
    0x06F2: 0x0420,
    0x06F3: 0x0421,
    0x06F4: 0x0422,
    0x06F5: 0x0423,
    0x06F6: 0x0416,
    0x06F7: 0x0412,
    0x06F8: 0x042C,
    0x06F9: 0x042B,
    0x06FA: 0x0417,
    0x06FB: 0x0428,
    0x06FC: 0x042D,
    0x06FD: 0x0429,
    0x06FE: 0x0427,
    0x06FF: 0x042A,
    0x07A1: 0x0386,
    0x07A2: 0x0388,
    0x07A3: 0x0389,
    0x07A4: 0x038A,
    0x07A5: 0x03AA,
    0x07A7: 0x038C,
    0x07A8: 0x038E,
    0x07A9: 0x03AB,
    0x07AB: 0x038F,
    0x07AE: 0x0385,
    0x07AF: 0x2015,
    0x07B1: 0x03AC,
    0x07B2: 0x03AD,
    0x07B3: 0x03AE,
    0x07B4: 0x03AF,
    0x07B5: 0x03CA,
    0x07B6: 0x0390,
    0x07B7: 0x03CC,
    0x07B8: 0x03CD,
    0x07B9: 0x03CB,
    0x07BA: 0x03B0,
    0x07BB: 0x03CE,
    0x07C1: 0x0391,
    0x07C2: 0x0392,
    0x07C3: 0x0393,
    0x07C4: 0x0394,
    0x07C5: 0x0395,
    0x07C6: 0x0396,
    0x07C7: 0x0397,
    0x07C8: 0x0398,
    0x07C9: 0x0399,
    0x07CA: 0x039A,
    0x07CB: 0x039B,
    0x07CC: 0x039C,
    0x07CD: 0x039D,
    0x07CE: 0x039E,
    0x07CF: 0x039F,
    0x07D0: 0x03A0,
    0x07D1: 0x03A1,
    0x07D2: 0x03A3,
    0x07D4: 0x03A4,
    0x07D5: 0x03A5,
    0x07D6: 0x03A6,
    0x07D7: 0x03A7,
    0x07D8: 0x03A8,
    0x07D9: 0x03A9,
    0x07E1: 0x03B1,
    0x07E2: 0x03B2,
    0x07E3: 0x03B3,
    0x07E4: 0x03B4,
    0x07E5: 0x03B5,
    0x07E6: 0x03B6,
    0x07E7: 0x03B7,
    0x07E8: 0x03B8,
    0x07E9: 0x03B9,
    0x07EA: 0x03BA,
    0x07EB: 0x03BB,
    0x07EC: 0x03BC,
    0x07ED: 0x03BD,
    0x07EE: 0x03BE,
    0x07EF: 0x03BF,
    0x07F0: 0x03C0,
    0x07F1: 0x03C1,
    0x07F2: 0x03C3,
    0x07F3: 0x03C2,
    0x07F4: 0x03C4,
    0x07F5: 0x03C5,
    0x07F6: 0x03C6,
    0x07F7: 0x03C7,
    0x07F8: 0x03C8,
    0x07F9: 0x03C9,
    0x08A1: 0x23B7,
    0x08A4: 0x2320,
    0x08A5: 0x2321,
    0x08A7: 0x23A1,
    0x08A8: 0x23A3,
    0x08A9: 0x23A4,
    0x08AA: 0x23A6,
    0x08AB: 0x239B,
    0x08AC: 0x239D,
    0x08AD: 0x239E,
    0x08AE: 0x23A0,
    0x08AF: 0x23A8,
    0x08B0: 0x23AC,
    0x08BC: 0x2264,
    0x08BD: 0x2260,
    0x08BE: 0x2265,
    0x08BF: 0x222B,
    0x08C0: 0x2234,
    0x08C1: 0x221D,
    0x08C2: 0x221E,
    0x08C5: 0x2207,
    0x08C8: 0x223C,
    0x08C9: 0x2243,
    0x08CD: 0x21D4,
    0x08CE: 0x21D2,
    0x08CF: 0x2261,
    0x08D6: 0x221A,
    0x08DA: 0x2282,
    0x08DB: 0x2283,
    0x08DC: 0x2229,
    0x08DD: 0x222A,
    0x08DE: 0x2227,
    0x08DF: 0x2228,
    0x08EF: 0x2202,
    0x08F6: 0x0192,
    0x08FB: 0x2190,
    0x08FC: 0x2191,
    0x08FD: 0x2192,
    0x08FE: 0x2193,
    0x09E0: 0x25C6,
    0x09E1: 0x2592,
    0x09E2: 0x2409,
    0x09E3: 0x240C,
    0x09E4: 0x240D,
    0x09E5: 0x240A,
    0x09E8: 0x2424,
    0x09E9: 0x240B,
    0x09EA: 0x2518,
    0x09EB: 0x2510,
    0x09EC: 0x250C,
    0x09ED: 0x2514,
    0x09EE: 0x253C,
    0x09EF: 0x23BA,
    0x09F0: 0x23BB,
    0x09F1: 0x2500,
    0x09F2: 0x23BC,
    0x09F3: 0x23BD,
    0x09F4: 0x251C,
    0x09F5: 0x2524,
    0x09F6: 0x2534,
    0x09F7: 0x252C,
    0x09F8: 0x2502,
    0x0AA1: 0x2003,
    0x0AA2: 0x2002,
    0x0AA3: 0x2004,
    0x0AA4: 0x2005,
    0x0AA5: 0x2007,
    0x0AA6: 0x2008,
    0x0AA7: 0x2009,
    0x0AA8: 0x200A,
    0x0AA9: 0x2014,
    0x0AAA: 0x2013,
    0x0AAE: 0x2026,
    0x0AAF: 0x2025,
    0x0AB0: 0x2153,
    0x0AB1: 0x2154,
    0x0AB2: 0x2155,
    0x0AB3: 0x2156,
    0x0AB4: 0x2157,
    0x0AB5: 0x2158,
    0x0AB6: 0x2159,
    0x0AB7: 0x215A,
    0x0AB8: 0x2105,
    0x0ABB: 0x2012,
    0x0AC3: 0x215B,
    0x0AC4: 0x215C,
    0x0AC5: 0x215D,
    0x0AC6: 0x215E,
    0x0AC9: 0x2122,
    0x0AD0: 0x2018,
    0x0AD1: 0x2019,
    0x0AD2: 0x201C,
    0x0AD3: 0x201D,
    0x0AD4: 0x211E,
    0x0AD6: 0x2032,
    0x0AD7: 0x2033,
    0x0AD9: 0x271D,
    0x0AEC: 0x2663,
    0x0AED: 0x2666,
    0x0AEE: 0x2665,
    0x0AF0: 0x2720,
    0x0AF1: 0x2020,
    0x0AF2: 0x2021,
    0x0AF3: 0x2713,
    0x0AF4: 0x2717,
    0x0AF5: 0x266F,
    0x0AF6: 0x266D,
    0x0AF7: 0x2642,
    0x0AF8: 0x2640,
    0x0AF9: 0x260E,
    0x0AFA: 0x2315,
    0x0AFB: 0x2117,
    0x0AFC: 0x2038,
    0x0AFD: 0x201A,
    0x0AFE: 0x201E,
    0x0BC2: 0x22A5,
    0x0BC4: 0x230A,
    0x0BCA: 0x2218,
    0x0BCC: 0x2395,
    0x0BCE: 0x22A4,
    0x0BCF: 0x25CB,
    0x0BD3: 0x2308,
    0x0BDC: 0x22A2,
    0x0BFC: 0x22A3,
    0x0CDF: 0x2017,
    0x0CE0: 0x05D0,
    0x0CE1: 0x05D1,
    0x0CE2: 0x05D2,
    0x0CE3: 0x05D3,
    0x0CE4: 0x05D4,
    0x0CE5: 0x05D5,
    0x0CE6: 0x05D6,
    0x0CE7: 0x05D7,
    0x0CE8: 0x05D8,
    0x0CE9: 0x05D9,
    0x0CEA: 0x05DA,
    0x0CEB: 0x05DB,
    0x0CEC: 0x05DC,
    0x0CED: 0x05DD,
    0x0CEE: 0x05DE,
    0x0CEF: 0x05DF,
    0x0CF0: 0x05E0,
    0x0CF1: 0x05E1,
    0x0CF2: 0x05E2,
    0x0CF3: 0x05E3,
    0x0CF4: 0x05E4,
    0x0CF5: 0x05E5,
    0x0CF6: 0x05E6,
    0x0CF7: 0x05E7,
    0x0CF8: 0x05E8,
    0x0CF9: 0x05E9,
    0x0CFA: 0x05EA,
    0x0DA1: 0x0E01,
    0x0DA2: 0x0E02,
    0x0DA3: 0x0E03,
    0x0DA4: 0x0E04,
    0x0DA5: 0x0E05,
    0x0DA6: 0x0E06,
    0x0DA7: 0x0E07,
    0x0DA8: 0x0E08,
    0x0DA9: 0x0E09,
    0x0DAA: 0x0E0A,
    0x0DAB: 0x0E0B,
    0x0DAC: 0x0E0C,
    0x0DAD: 0x0E0D,
    0x0DAE: 0x0E0E,
    0x0DAF: 0x0E0F,
    0x0DB0: 0x0E10,
    0x0DB1: 0x0E11,
    0x0DB2: 0x0E12,
    0x0DB3: 0x0E13,
    0x0DB4: 0x0E14,
    0x0DB5: 0x0E15,
    0x0DB6: 0x0E16,
    0x0DB7: 0x0E17,
    0x0DB8: 0x0E18,
    0x0DB9: 0x0E19,
    0x0DBA: 0x0E1A,
    0x0DBB: 0x0E1B,
    0x0DBC: 0x0E1C,
    0x0DBD: 0x0E1D,
    0x0DBE: 0x0E1E,
    0x0DBF: 0x0E1F,
    0x0DC0: 0x0E20,
    0x0DC1: 0x0E21,
    0x0DC2: 0x0E22,
    0x0DC3: 0x0E23,
    0x0DC4: 0x0E24,
    0x0DC5: 0x0E25,
    0x0DC6: 0x0E26,
    0x0DC7: 0x0E27,
    0x0DC8: 0x0E28,
    0x0DC9: 0x0E29,
    0x0DCA: 0x0E2A,
    0x0DCB: 0x0E2B,
    0x0DCC: 0x0E2C,
    0x0DCD: 0x0E2D,
    0x0DCE: 0x0E2E,
    0x0DCF: 0x0E2F,
    0x0DD0: 0x0E30,
    0x0DD1: 0x0E31,
    0x0DD2: 0x0E32,
    0x0DD3: 0x0E33,
    0x0DD4: 0x0E34,
    0x0DD5: 0x0E35,
    0x0DD6: 0x0E36,
    0x0DD7: 0x0E37,
    0x0DD8: 0x0E38,
    0x0DD9: 0x0E39,
    0x0DDA: 0x0E3A,
    0x0DDF: 0x0E3F,
    0x0DE0: 0x0E40,
    0x0DE1: 0x0E41,
    0x0DE2: 0x0E42,
    0x0DE3: 0x0E43,
    0x0DE4: 0x0E44,
    0x0DE5: 0x0E45,
    0x0DE6: 0x0E46,
    0x0DE7: 0x0E47,
    0x0DE8: 0x0E48,
    0x0DE9: 0x0E49,
    0x0DEA: 0x0E4A,
    0x0DEB: 0x0E4B,
    0x0DEC: 0x0E4C,
    0x0DED: 0x0E4D,
    0x0DF0: 0x0E50,
    0x0DF1: 0x0E51,
    0x0DF2: 0x0E52,
    0x0DF3: 0x0E53,
    0x0DF4: 0x0E54,
    0x0DF5: 0x0E55,
    0x0DF6: 0x0E56,
    0x0DF7: 0x0E57,
    0x0DF8: 0x0E58,
    0x0DF9: 0x0E59,
    0x13BC: 0x0152,
    0x13BD: 0x0153,
    0x13BE: 0x0178,
    0x20AC: 0x20AC,
    }

_KEYSYMS = {
    'space': 0x20,
    'exclam': 0x21,
    'quotedbl': 0x22,
    'numbersign': 0x23,
    'dollar': 0x24,
    'percent': 0x25,
    'ampersand': 0x26,
    'apostrophe': 0x27,
    'parenleft': 0x28,
    'parenright': 0x29,
    'asterisk': 0x2a,
    'plus': 0x2b,
    'comma': 0x2c,
    'minus': 0x2d,
    'period': 0x2e,
    'slash': 0x2f,
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,
    'colon': 0x3a,
    'semicolon': 0x3b,
    'less': 0x3c,
    'equal': 0x3d,
    'greater': 0x3e,
    'question': 0x3f,
    'at': 0x40,
    'A': 0x41,
    'B': 0x42,
    'C': 0x43,
    'D': 0x44,
    'E': 0x45,
    'F': 0x46,
    'G': 0x47,
    'H': 0x48,
    'I': 0x49,
    'J': 0x4a,
    'K': 0x4b,
    'L': 0x4c,
    'M': 0x4d,
    'N': 0x4e,
    'O': 0x4f,
    'P': 0x50,
    'Q': 0x51,
    'R': 0x52,
    'S': 0x53,
    'T': 0x54,
    'U': 0x55,
    'V': 0x56,
    'W': 0x57,
    'X': 0x58,
    'Y': 0x59,
    'Z': 0x5a,
    'bracketleft': 0x5b,
    'backslash': 0x5c,
    'bracketright': 0x5d,
    'asciicircum': 0x5e,
    'underscore': 0x5f,
    'quoteleft': 0x60,
    'a': 0x61,
    'b': 0x62,
    'c': 0x63,
    'd': 0x64,
    'e': 0x65,
    'f': 0x66,
    'g': 0x67,
    'h': 0x68,
    'i': 0x69,
    'j': 0x6a,
    'k': 0x6b,
    'l': 0x6c,
    'm': 0x6d,
    'n': 0x6e,
    'o': 0x6f,
    'p': 0x70,
    'q': 0x71,
    'r': 0x72,
    's': 0x73,
    't': 0x74,
    'u': 0x75,
    'v': 0x76,
    'w': 0x77,
    'x': 0x78,
    'y': 0x79,
    'z': 0x7a,
    'braceleft': 0x7b,
    'bar': 0x7c,
    'braceright': 0x7d,
    'asciitilde': 0x7e,
    'nobreakspace': 0xa0,
    'exclamdown': 0xa1,
    'cent': 0xa2,
    'sterling': 0xa3,
    'currency': 0xa4,
    'yen': 0xa5,
    'brokenbar': 0xa6,
    'section': 0xa7,
    'diaeresis': 0xa8,
    'copyright': 0xa9,
    'ordfeminine': 0xaa,
    'guillemotleft': 0xab,
    'notsign': 0xac,
    'hyphen': 0xad,
    'registered': 0xae,
    'macron': 0xaf,
    'degree': 0xb0,
    'plusminus': 0xb1,
    'twosuperior': 0xb2,
    'threesuperior': 0xb3,
    'acute': 0xb4,
    'mu': 0xb5,
    'paragraph': 0xb6,
    'periodcentered': 0xb7,
    'cedilla': 0xb8,
    'onesuperior': 0xb9,
    'masculine': 0xba,
    'guillemotright': 0xbb,
    'onequarter': 0xbc,
    'onehalf': 0xbd,
    'threequarters': 0xbe,
    'questiondown': 0xbf,
    'Agrave': 0xc0,
    'Aacute': 0xc1,
    'Acircumflex': 0xc2,
    'Atilde': 0xc3,
    'Adiaeresis': 0xc4,
    'Aring': 0xc5,
    'AE': 0xc6,
    'Ccedilla': 0xc7,
    'Egrave': 0xc8,
    'Eacute': 0xc9,
    'Ecircumflex': 0xca,
    'Ediaeresis': 0xcb,
    'Igrave': 0xcc,
    'Iacute': 0xcd,
    'Icircumflex': 0xce,
    'Idiaeresis': 0xcf,
    'Eth': 0xd0,
    'Ntilde': 0xd1,
    'Ograve': 0xd2,
    'Oacute': 0xd3,
    'Ocircumflex': 0xd4,
    'Otilde': 0xd5,
    'Odiaeresis': 0xd6,
    'multiply': 0xd7,
    'Oslash': 0xd8,
    'Ugrave': 0xd9,
    'Uacute': 0xda,
    'Ucircumflex': 0xdb,
    'Udiaeresis': 0xdc,
    'Yacute': 0xdd,
    'Thorn': 0xde,
    'ssharp': 0xdf,
    'agrave': 0xe0,
    'aacute': 0xe1,
    'acircumflex': 0xe2,
    'atilde': 0xe3,
    'adiaeresis': 0xe4,
    'aring': 0xe5,
    'ae': 0xe6,
    'ccedilla': 0xe7,
    'egrave': 0xe8,
    'eacute': 0xe9,
    'ecircumflex': 0xea,
    'ediaeresis': 0xeb,
    'igrave': 0xec,
    'iacute': 0xed,
    'icircumflex': 0xee,
    'idiaeresis': 0xef,
    'eth': 0xf0,
    'ntilde': 0xf1,
    'ograve': 0xf2,
    'oacute': 0xf3,
    'ocircumflex': 0xf4,
    'otilde': 0xf5,
    'odiaeresis': 0xf6,
    'division': 0xf7,
    'ooblique': 0xf8,
    'ugrave': 0xf9,
    'uacute': 0xfa,
    'ucircumflex': 0xfb,
    'udiaeresis': 0xfc,
    'yacute': 0xfd,
    'thorn': 0xfe,
    'ydiaeresis': 0xff,
    'Aogonek': 0x1a1,
    'breve': 0x1a2,
    'Lstroke': 0x1a3,
    'Lcaron': 0x1a5,
    'Sacute': 0x1a6,
    'Scaron': 0x1a9,
    'Scedilla': 0x1aa,
    'Tcaron': 0x1ab,
    'Zacute': 0x1ac,
    'Zcaron': 0x1ae,
    'Zabovedot': 0x1af,
    'aogonek': 0x1b1,
    'ogonek': 0x1b2,
    'lstroke': 0x1b3,
    'lcaron': 0x1b5,
    'sacute': 0x1b6,
    'caron': 0x1b7,
    'scaron': 0x1b9,
    'scedilla': 0x1ba,
    'tcaron': 0x1bb,
    'zacute': 0x1bc,
    'doubleacute': 0x1bd,
    'zcaron': 0x1be,
    'zabovedot': 0x1bf,
    'Racute': 0x1c0,
    'Abreve': 0x1c3,
    'Lacute': 0x1c5,
    'Cacute': 0x1c6,
    'Ccaron': 0x1c8,
    'Eogonek': 0x1ca,
    'Ecaron': 0x1cc,
    'Dcaron': 0x1cf,
    'Dstroke': 0x1d0,
    'Nacute': 0x1d1,
    'Ncaron': 0x1d2,
    'Odoubleacute': 0x1d5,
    'Rcaron': 0x1d8,
    'Uring': 0x1d9,
    'Udoubleacute': 0x1db,
    'Tcedilla': 0x1de,
    'racute': 0x1e0,
    'abreve': 0x1e3,
    'lacute': 0x1e5,
    'cacute': 0x1e6,
    'ccaron': 0x1e8,
    'eogonek': 0x1ea,
    'ecaron': 0x1ec,
    'dcaron': 0x1ef,
    'dstroke': 0x1f0,
    'nacute': 0x1f1,
    'ncaron': 0x1f2,
    'odoubleacute': 0x1f5,
    'rcaron': 0x1f8,
    'uring': 0x1f9,
    'udoubleacute': 0x1fb,
    'tcedilla': 0x1fe,
    'abovedot': 0x1ff,
    'Hstroke': 0x2a1,
    'Hcircumflex': 0x2a6,
    'Iabovedot': 0x2a9,
    'Gbreve': 0x2ab,
    'Jcircumflex': 0x2ac,
    'hstroke': 0x2b1,
    'hcircumflex': 0x2b6,
    'idotless': 0x2b9,
    'gbreve': 0x2bb,
    'jcircumflex': 0x2bc,
    'Cabovedot': 0x2c5,
    'Ccircumflex': 0x2c6,
    'Gabovedot': 0x2d5,
    'Gcircumflex': 0x2d8,
    'Ubreve': 0x2dd,
    'Scircumflex': 0x2de,
    'cabovedot': 0x2e5,
    'ccircumflex': 0x2e6,
    'gabovedot': 0x2f5,
    'gcircumflex': 0x2f8,
    'ubreve': 0x2fd,
    'scircumflex': 0x2fe,
    'kra': 0x3a2,
    'Rcedilla': 0x3a3,
    'Itilde': 0x3a5,
    'Lcedilla': 0x3a6,
    'Emacron': 0x3aa,
    'Gcedilla': 0x3ab,
    'Tslash': 0x3ac,
    'rcedilla': 0x3b3,
    'itilde': 0x3b5,
    'lcedilla': 0x3b6,
    'emacron': 0x3ba,
    'gcedilla': 0x3bb,
    'tslash': 0x3bc,
    'ENG': 0x3bd,
    'eng': 0x3bf,
    'Amacron': 0x3c0,
    'Iogonek': 0x3c7,
    'Eabovedot': 0x3cc,
    'Imacron': 0x3cf,
    'Ncedilla': 0x3d1,
    'Omacron': 0x3d2,
    'Kcedilla': 0x3d3,
    'Uogonek': 0x3d9,
    'Utilde': 0x3dd,
    'Umacron': 0x3de,
    'amacron': 0x3e0,
    'iogonek': 0x3e7,
    'eabovedot': 0x3ec,
    'imacron': 0x3ef,
    'ncedilla': 0x3f1,
    'omacron': 0x3f2,
    'kcedilla': 0x3f3,
    'uogonek': 0x3f9,
    'utilde': 0x3fd,
    'umacron': 0x3fe,
    'overline': 0x47e,
    'kana_fullstop': 0x4a1,
    'kana_openingbracket': 0x4a2,
    'kana_closingbracket': 0x4a3,
    'kana_comma': 0x4a4,
    'kana_conjunctive': 0x4a5,
    'kana_WO': 0x4a6,
    'kana_a': 0x4a7,
    'kana_i': 0x4a8,
    'kana_u': 0x4a9,
    'kana_e': 0x4aa,
    'kana_o': 0x4ab,
    'kana_ya': 0x4ac,
    'kana_yu': 0x4ad,
    'kana_yo': 0x4ae,
    'kana_tsu': 0x4af,
    'prolongedsound': 0x4b0,
    'kana_A': 0x4b1,
    'kana_I': 0x4b2,
    'kana_U': 0x4b3,
    'kana_E': 0x4b4,
    'kana_O': 0x4b5,
    'kana_KA': 0x4b6,
    'kana_KI': 0x4b7,
    'kana_KU': 0x4b8,
    'kana_KE': 0x4b9,
    'kana_KO': 0x4ba,
    'kana_SA': 0x4bb,
    'kana_SHI': 0x4bc,
    'kana_SU': 0x4bd,
    'kana_SE': 0x4be,
    'kana_SO': 0x4bf,
    'kana_TA': 0x4c0,
    'kana_TI': 0x4c1,
    'kana_TSU': 0x4c2,
    'kana_TE': 0x4c3,
    'kana_TO': 0x4c4,
    'kana_NA': 0x4c5,
    'kana_NI': 0x4c6,
    'kana_NU': 0x4c7,
    'kana_NE': 0x4c8,
    'kana_NO': 0x4c9,
    'kana_HA': 0x4ca,
    'kana_HI': 0x4cb,
    'kana_HU': 0x4cc,
    'kana_HE': 0x4cd,
    'kana_HO': 0x4ce,
    'kana_MA': 0x4cf,
    'kana_MI': 0x4d0,
    'kana_MU': 0x4d1,
    'kana_ME': 0x4d2,
    'kana_MO': 0x4d3,
    'kana_YA': 0x4d4,
    'kana_YU': 0x4d5,
    'kana_YO': 0x4d6,
    'kana_RA': 0x4d7,
    'kana_RI': 0x4d8,
    'kana_RU': 0x4d9,
    'kana_RE': 0x4da,
    'kana_RO': 0x4db,
    'kana_WA': 0x4dc,
    'kana_N': 0x4dd,
    'voicedsound': 0x4de,
    'semivoicedsound': 0x4df,
    'Arabic_comma': 0x5ac,
    'Arabic_semicolon': 0x5bb,
    'Arabic_question_mark': 0x5bf,
    'Arabic_hamza': 0x5c1,
    'Arabic_maddaonalef': 0x5c2,
    'Arabic_hamzaonalef': 0x5c3,
    'Arabic_hamzaonwaw': 0x5c4,
    'Arabic_hamzaunderalef': 0x5c5,
    'Arabic_hamzaonyeh': 0x5c6,
    'Arabic_alef': 0x5c7,
    'Arabic_beh': 0x5c8,
    'Arabic_tehmarbuta': 0x5c9,
    'Arabic_teh': 0x5ca,
    'Arabic_theh': 0x5cb,
    'Arabic_jeem': 0x5cc,
    'Arabic_hah': 0x5cd,
    'Arabic_khah': 0x5ce,
    'Arabic_dal': 0x5cf,
    'Arabic_thal': 0x5d0,
    'Arabic_ra': 0x5d1,
    'Arabic_zain': 0x5d2,
    'Arabic_seen': 0x5d3,
    'Arabic_sheen': 0x5d4,
    'Arabic_sad': 0x5d5,
    'Arabic_dad': 0x5d6,
    'Arabic_tah': 0x5d7,
    'Arabic_zah': 0x5d8,
    'Arabic_ain': 0x5d9,
    'Arabic_ghain': 0x5da,
    'Arabic_tatweel': 0x5e0,
    'Arabic_feh': 0x5e1,
    'Arabic_qaf': 0x5e2,
    'Arabic_kaf': 0x5e3,
    'Arabic_lam': 0x5e4,
    'Arabic_meem': 0x5e5,
    'Arabic_noon': 0x5e6,
    'Arabic_ha': 0x5e7,
    'Arabic_waw': 0x5e8,
    'Arabic_alefmaksura': 0x5e9,
    'Arabic_yeh': 0x5ea,
    'Arabic_fathatan': 0x5eb,
    'Arabic_dammatan': 0x5ec,
    'Arabic_kasratan': 0x5ed,
    'Arabic_fatha': 0x5ee,
    'Arabic_damma': 0x5ef,
    'Arabic_kasra': 0x5f0,
    'Arabic_shadda': 0x5f1,
    'Arabic_sukun': 0x5f2,
    'Serbian_dje': 0x6a1,
    'Macedonia_gje': 0x6a2,
    'Cyrillic_io': 0x6a3,
    'Ukranian_je': 0x6a4,
    'Macedonia_dse': 0x6a5,
    'Ukranian_i': 0x6a6,
    'Ukranian_yi': 0x6a7,
    'Cyrillic_je': 0x6a8,
    'Serbian_lje': 0x6a9,
    'Serbian_nje': 0x6aa,
    'Serbian_tshe': 0x6ab,
    'Macedonia_kje': 0x6ac,
    'Ukrainian_ghe_with_upturn': 0x6ad,
    'Byelorussian_shortu': 0x6ae,
    'Cyrillic_dzhe': 0x6af,
    'numerosign': 0x6b0,
    'Serbian_DJE': 0x6b1,
    'Macedonia_GJE': 0x6b2,
    'Cyrillic_IO': 0x6b3,
    'Ukranian_JE': 0x6b4,
    'Macedonia_DSE': 0x6b5,
    'Ukranian_I': 0x6b6,
    'Ukrainian_YI': 0x6b7,
    'Serbian_JE': 0x6b8,
    'Cyrillic_LJE': 0x6b9,
    'Serbian_NJE': 0x6ba,
    'Serbian_TSHE': 0x6bb,
    'Macedonia_KJE': 0x6bc,
    'Ukrainian_GHE_WITH_UPTURN': 0x6bd,
    'Byelorussian_SHORTU': 0x6be,
    'Serbian_DZE': 0x6bf,
    'Cyrillic_yu': 0x6c0,
    'Cyrillic_a': 0x6c1,
    'Cyrillic_be': 0x6c2,
    'Cyrillic_tse': 0x6c3,
    'Cyrillic_de': 0x6c4,
    'Cyrillic_ie': 0x6c5,
    'Cyrillic_ef': 0x6c6,
    'Cyrillic_ghe': 0x6c7,
    'Cyrillic_ha': 0x6c8,
    'Cyrillic_i': 0x6c9,
    'Cyrillic_shorti': 0x6ca,
    'Cyrillic_ka': 0x6cb,
    'Cyrillic_el': 0x6cc,
    'Cyrillic_em': 0x6cd,
    'Cyrillic_en': 0x6ce,
    'Cyrillic_o': 0x6cf,
    'Cyrillic_pe': 0x6d0,
    'Cyrillic_ya': 0x6d1,
    'Cyrillic_er': 0x6d2,
    'Cyrillic_es': 0x6d3,
    'Cyrillic_te': 0x6d4,
    'Cyrillic_u': 0x6d5,
    'Cyrillic_zhe': 0x6d6,
    'Cyrillic_ve': 0x6d7,
    'Cyrillic_softsign': 0x6d8,
    'Cyrillic_yeru': 0x6d9,
    'Cyrillic_ze': 0x6da,
    'Cyrillic_sha': 0x6db,
    'Cyrillic_e': 0x6dc,
    'Cyrillic_shcha': 0x6dd,
    'Cyrillic_che': 0x6de,
    'Cyrillic_hardsign': 0x6df,
    'Cyrillic_YU': 0x6e0,
    'Cyrillic_A': 0x6e1,
    'Cyrillic_BE': 0x6e2,
    'Cyrillic_TSE': 0x6e3,
    'Cyrillic_DE': 0x6e4,
    'Cyrillic_IE': 0x6e5,
    'Cyrillic_EF': 0x6e6,
    'Cyrillic_GHE': 0x6e7,
    'Cyrillic_HA': 0x6e8,
    'Cyrillic_I': 0x6e9,
    'Cyrillic_SHORTI': 0x6ea,
    'Cyrillic_KA': 0x6eb,
    'Cyrillic_EL': 0x6ec,
    'Cyrillic_EM': 0x6ed,
    'Cyrillic_EN': 0x6ee,
    'Cyrillic_O': 0x6ef,
    'Cyrillic_PE': 0x6f0,
    'Cyrillic_YA': 0x6f1,
    'Cyrillic_ER': 0x6f2,
    'Cyrillic_ES': 0x6f3,
    'Cyrillic_TE': 0x6f4,
    'Cyrillic_U': 0x6f5,
    'Cyrillic_ZHE': 0x6f6,
    'Cyrillic_VE': 0x6f7,
    'Cyrillic_SOFTSIGN': 0x6f8,
    'Cyrillic_YERU': 0x6f9,
    'Cyrillic_ZE': 0x6fa,
    'Cyrillic_SHA': 0x6fb,
    'Cyrillic_E': 0x6fc,
    'Cyrillic_SHCHA': 0x6fd,
    'Cyrillic_CHE': 0x6fe,
    'Cyrillic_HARDSIGN': 0x6ff,
    'Greek_ALPHAaccent': 0x7a1,
    'Greek_EPSILONaccent': 0x7a2,
    'Greek_ETAaccent': 0x7a3,
    'Greek_IOTAaccent': 0x7a4,
    'Greek_IOTAdiaeresis': 0x7a5,
    'Greek_OMICRONaccent': 0x7a7,
    'Greek_UPSILONaccent': 0x7a8,
    'Greek_UPSILONdieresis': 0x7a9,
    'Greek_OMEGAaccent': 0x7ab,
    'Greek_accentdieresis': 0x7ae,
    'Greek_horizbar': 0x7af,
    'Greek_alphaaccent': 0x7b1,
    'Greek_epsilonaccent': 0x7b2,
    'Greek_etaaccent': 0x7b3,
    'Greek_iotaaccent': 0x7b4,
    'Greek_iotadieresis': 0x7b5,
    'Greek_iotaaccentdieresis': 0x7b6,
    'Greek_omicronaccent': 0x7b7,
    'Greek_upsilonaccent': 0x7b8,
    'Greek_upsilondieresis': 0x7b9,
    'Greek_upsilonaccentdieresis': 0x7ba,
    'Greek_omegaaccent': 0x7bb,
    'Greek_ALPHA': 0x7c1,
    'Greek_BETA': 0x7c2,
    'Greek_GAMMA': 0x7c3,
    'Greek_DELTA': 0x7c4,
    'Greek_EPSILON': 0x7c5,
    'Greek_ZETA': 0x7c6,
    'Greek_ETA': 0x7c7,
    'Greek_THETA': 0x7c8,
    'Greek_IOTA': 0x7c9,
    'Greek_KAPPA': 0x7ca,
    'Greek_LAMBDA': 0x7cb,
    'Greek_MU': 0x7cc,
    'Greek_NU': 0x7cd,
    'Greek_XI': 0x7ce,
    'Greek_OMICRON': 0x7cf,
    'Greek_PI': 0x7d0,
    'Greek_RHO': 0x7d1,
    'Greek_SIGMA': 0x7d2,
    'Greek_TAU': 0x7d4,
    'Greek_UPSILON': 0x7d5,
    'Greek_PHI': 0x7d6,
    'Greek_CHI': 0x7d7,
    'Greek_PSI': 0x7d8,
    'Greek_OMEGA': 0x7d9,
    'Greek_alpha': 0x7e1,
    'Greek_beta': 0x7e2,
    'Greek_gamma': 0x7e3,
    'Greek_delta': 0x7e4,
    'Greek_epsilon': 0x7e5,
    'Greek_zeta': 0x7e6,
    'Greek_eta': 0x7e7,
    'Greek_theta': 0x7e8,
    'Greek_iota': 0x7e9,
    'Greek_kappa': 0x7ea,
    'Greek_lamda': 0x7eb,
    'Greek_mu': 0x7ec,
    'Greek_nu': 0x7ed,
    'Greek_xi': 0x7ee,
    'Greek_omicron': 0x7ef,
    'Greek_pi': 0x7f0,
    'Greek_rho': 0x7f1,
    'Greek_sigma': 0x7f2,
    'Greek_finalsmallsigma': 0x7f3,
    'Greek_tau': 0x7f4,
    'Greek_upsilon': 0x7f5,
    'Greek_phi': 0x7f6,
    'Greek_chi': 0x7f7,
    'Greek_psi': 0x7f8,
    'Greek_omega': 0x7f9,
    'leftradical': 0x8a1,
    'topleftradical': 0x8a2,
    'horizconnector': 0x8a3,
    'topintegral': 0x8a4,
    'botintegral': 0x8a5,
    'vertconnector': 0x8a6,
    'topleftsqbracket': 0x8a7,
    'botleftsqbracket': 0x8a8,
    'toprightsqbracket': 0x8a9,
    'botrightsqbracket': 0x8aa,
    'topleftparens': 0x8ab,
    'botleftparens': 0x8ac,
    'toprightparens': 0x8ad,
    'botrightparens': 0x8ae,
    'leftmiddlecurlybrace': 0x8af,
    'rightmiddlecurlybrace': 0x8b0,
    'topleftsummation': 0x8b1,
    'botleftsummation': 0x8b2,
    'topvertsummationconnector': 0x8b3,
    'botvertsummationconnector': 0x8b4,
    'toprightsummation': 0x8b5,
    'botrightsummation': 0x8b6,
    'rightmiddlesummation': 0x8b7,
    'lessthanequal': 0x8bc,
    'notequal': 0x8bd,
    'greaterthanequal': 0x8be,
    'integral': 0x8bf,
    'therefore': 0x8c0,
    'variation': 0x8c1,
    'infinity': 0x8c2,
    'nabla': 0x8c5,
    'approximate': 0x8c8,
    'similarequal': 0x8c9,
    'ifonlyif': 0x8cd,
    'implies': 0x8ce,
    'identical': 0x8cf,
    'radical': 0x8d6,
    'includedin': 0x8da,
    'includes': 0x8db,
    'intersection': 0x8dc,
    'union': 0x8dd,
    'logicaland': 0x8de,
    'logicalor': 0x8df,
    'partialderivative': 0x8ef,
    'function': 0x8f6,
    'leftarrow': 0x8fb,
    'uparrow': 0x8fc,
    'rightarrow': 0x8fd,
    'downarrow': 0x8fe,
    'blank': 0x9df,
    'soliddiamond': 0x9e0,
    'checkerboard': 0x9e1,
    'ht': 0x9e2,
    'ff': 0x9e3,
    'cr': 0x9e4,
    'lf': 0x9e5,
    'nl': 0x9e8,
    'vt': 0x9e9,
    'lowrightcorner': 0x9ea,
    'uprightcorner': 0x9eb,
    'upleftcorner': 0x9ec,
    'lowleftcorner': 0x9ed,
    'crossinglines': 0x9ee,
    'horizlinescan1': 0x9ef,
    'horizlinescan3': 0x9f0,
    'horizlinescan5': 0x9f1,
    'horizlinescan7': 0x9f2,
    'horizlinescan9': 0x9f3,
    'leftt': 0x9f4,
    'rightt': 0x9f5,
    'bott': 0x9f6,
    'topt': 0x9f7,
    'vertbar': 0x9f8,
    'emspace': 0xaa1,
    'enspace': 0xaa2,
    'em3space': 0xaa3,
    'em4space': 0xaa4,
    'digitspace': 0xaa5,
    'punctspace': 0xaa6,
    'thinspace': 0xaa7,
    'hairspace': 0xaa8,
    'emdash': 0xaa9,
    'endash': 0xaaa,
    'signifblank': 0xaac,
    'ellipsis': 0xaae,
    'doubbaselinedot': 0xaaf,
    'onethird': 0xab0,
    'twothirds': 0xab1,
    'onefifth': 0xab2,
    'twofifths': 0xab3,
    'threefifths': 0xab4,
    'fourfifths': 0xab5,
    'onesixth': 0xab6,
    'fivesixths': 0xab7,
    'careof': 0xab8,
    'figdash': 0xabb,
    'leftanglebracket': 0xabc,
    'decimalpoint': 0xabd,
    'rightanglebracket': 0xabe,
    'marker': 0xabf,
    'oneeighth': 0xac3,
    'threeeighths': 0xac4,
    'fiveeighths': 0xac5,
    'seveneighths': 0xac6,
    'trademark': 0xac9,
    'signaturemark': 0xaca,
    'trademarkincircle': 0xacb,
    'leftopentriangle': 0xacc,
    'rightopentriangle': 0xacd,
    'emopencircle': 0xace,
    'emopenrectangle': 0xacf,
    'leftsinglequotemark': 0xad0,
    'rightsinglequotemark': 0xad1,
    'leftdoublequotemark': 0xad2,
    'rightdoublequotemark': 0xad3,
    'prescription': 0xad4,
    'permille': 0xad5,
    'minutes': 0xad6,
    'seconds': 0xad7,
    'latincross': 0xad9,
    'hexagram': 0xada,
    'filledrectbullet': 0xadb,
    'filledlefttribullet': 0xadc,
    'filledrighttribullet': 0xadd,
    'emfilledcircle': 0xade,
    'emfilledrect': 0xadf,
    'enopencircbullet': 0xae0,
    'enopensquarebullet': 0xae1,
    'openrectbullet': 0xae2,
    'opentribulletup': 0xae3,
    'opentribulletdown': 0xae4,
    'openstar': 0xae5,
    'enfilledcircbullet': 0xae6,
    'enfilledsqbullet': 0xae7,
    'filledtribulletup': 0xae8,
    'filledtribulletdown': 0xae9,
    'leftpointer': 0xaea,
    'rightpointer': 0xaeb,
    'club': 0xaec,
    'diamond': 0xaed,
    'heart': 0xaee,
    'maltesecross': 0xaf0,
    'dagger': 0xaf1,
    'doubledagger': 0xaf2,
    'checkmark': 0xaf3,
    'ballotcross': 0xaf4,
    'musicalsharp': 0xaf5,
    'musicalflat': 0xaf6,
    'malesymbol': 0xaf7,
    'femalesymbol': 0xaf8,
    'telephone': 0xaf9,
    'telephonerecorder': 0xafa,
    'phonographcopyright': 0xafb,
    'caret': 0xafc,
    'singlelowquotemark': 0xafd,
    'doublelowquotemark': 0xafe,
    'cursor': 0xaff,
    'leftcaret': 0xba3,
    'rightcaret': 0xba6,
    'downcaret': 0xba8,
    'upcaret': 0xba9,
    'overbar': 0xbc0,
    'downtack': 0xbc2,
    'upshoe': 0xbc3,
    'downstile': 0xbc4,
    'underbar': 0xbc6,
    'jot': 0xbca,
    'quad': 0xbcc,
    'uptack': 0xbce,
    'circle': 0xbcf,
    'upstile': 0xbd3,
    'downshoe': 0xbd6,
    'rightshoe': 0xbd8,
    'leftshoe': 0xbda,
    'lefttack': 0xbdc,
    'righttack': 0xbfc,
    'hebrew_doublelowline': 0xcdf,
    'hebrew_aleph': 0xce0,
    'hebrew_bet': 0xce1,
    'hebrew_gimel': 0xce2,
    'hebrew_daleth': 0xce3,
    'hebrew_he': 0xce4,
    'hebrew_waw': 0xce5,
    'hebrew_zayin': 0xce6,
    'hebrew_chet': 0xce7,
    'hebrew_tet': 0xce8,
    'hebrew_yod': 0xce9,
    'hebrew_finalkaph': 0xcea,
    'hebrew_kaph': 0xceb,
    'hebrew_lamed': 0xcec,
    'hebrew_finalmem': 0xced,
    'hebrew_mem': 0xcee,
    'hebrew_finalnun': 0xcef,
    'hebrew_nun': 0xcf0,
    'hebrew_samech': 0xcf1,
    'hebrew_ayin': 0xcf2,
    'hebrew_finalpe': 0xcf3,
    'hebrew_pe': 0xcf4,
    'hebrew_finalzadi': 0xcf5,
    'hebrew_zadi': 0xcf6,
    'hebrew_kuf': 0xcf7,
    'hebrew_resh': 0xcf8,
    'hebrew_shin': 0xcf9,
    'hebrew_taf': 0xcfa,
    'Thai_kokai': 0xda1,
    'Thai_khokhai': 0xda2,
    'Thai_khokhuat': 0xda3,
    'Thai_khokhwai': 0xda4,
    'Thai_khokhon': 0xda5,
    'Thai_khorakhang': 0xda6,
    'Thai_ngongu': 0xda7,
    'Thai_chochan': 0xda8,
    'Thai_choching': 0xda9,
    'Thai_chochang': 0xdaa,
    'Thai_soso': 0xdab,
    'Thai_chochoe': 0xdac,
    'Thai_yoying': 0xdad,
    'Thai_dochada': 0xdae,
    'Thai_topatak': 0xdaf,
    'Thai_thothan': 0xdb0,
    'Thai_thonangmontho': 0xdb1,
    'Thai_thophuthao': 0xdb2,
    'Thai_nonen': 0xdb3,
    'Thai_dodek': 0xdb4,
    'Thai_totao': 0xdb5,
    'Thai_thothung': 0xdb6,
    'Thai_thothahan': 0xdb7,
    'Thai_thothong': 0xdb8,
    'Thai_nonu': 0xdb9,
    'Thai_bobaimai': 0xdba,
    'Thai_popla': 0xdbb,
    'Thai_phophung': 0xdbc,
    'Thai_fofa': 0xdbd,
    'Thai_phophan': 0xdbe,
    'Thai_fofan': 0xdbf,
    'Thai_phosamphao': 0xdc0,
    'Thai_moma': 0xdc1,
    'Thai_yoyak': 0xdc2,
    'Thai_rorua': 0xdc3,
    'Thai_ru': 0xdc4,
    'Thai_loling': 0xdc5,
    'Thai_lu': 0xdc6,
    'Thai_wowaen': 0xdc7,
    'Thai_sosala': 0xdc8,
    'Thai_sorusi': 0xdc9,
    'Thai_sosua': 0xdca,
    'Thai_hohip': 0xdcb,
    'Thai_lochula': 0xdcc,
    'Thai_oang': 0xdcd,
    'Thai_honokhuk': 0xdce,
    'Thai_paiyannoi': 0xdcf,
    'Thai_saraa': 0xdd0,
    'Thai_maihanakat': 0xdd1,
    'Thai_saraaa': 0xdd2,
    'Thai_saraam': 0xdd3,
    'Thai_sarai': 0xdd4,
    'Thai_saraii': 0xdd5,
    'Thai_saraue': 0xdd6,
    'Thai_sarauee': 0xdd7,
    'Thai_sarau': 0xdd8,
    'Thai_sarauu': 0xdd9,
    'Thai_phinthu': 0xdda,
    'Thai_maihanakat_maitho': 0xdde,
    'Thai_baht': 0xddf,
    'Thai_sarae': 0xde0,
    'Thai_saraae': 0xde1,
    'Thai_sarao': 0xde2,
    'Thai_saraaimaimuan': 0xde3,
    'Thai_saraaimaimalai': 0xde4,
    'Thai_lakkhangyao': 0xde5,
    'Thai_maiyamok': 0xde6,
    'Thai_maitaikhu': 0xde7,
    'Thai_maiek': 0xde8,
    'Thai_maitho': 0xde9,
    'Thai_maitri': 0xdea,
    'Thai_maichattawa': 0xdeb,
    'Thai_thanthakhat': 0xdec,
    'Thai_nikhahit': 0xded,
    'Thai_leksun': 0xdf0,
    'Thai_leknung': 0xdf1,
    'Thai_leksong': 0xdf2,
    'Thai_leksam': 0xdf3,
    'Thai_leksi': 0xdf4,
    'Thai_lekha': 0xdf5,
    'Thai_lekhok': 0xdf6,
    'Thai_lekchet': 0xdf7,
    'Thai_lekpaet': 0xdf8,
    'Thai_lekkao': 0xdf9,
    'Hangul_Kiyeog': 0xea1,
    'Hangul_SsangKiyeog': 0xea2,
    'Hangul_KiyeogSios': 0xea3,
    'Hangul_Nieun': 0xea4,
    'Hangul_NieunJieuj': 0xea5,
    'Hangul_NieunHieuh': 0xea6,
    'Hangul_Dikeud': 0xea7,
    'Hangul_SsangDikeud': 0xea8,
    'Hangul_Rieul': 0xea9,
    'Hangul_RieulKiyeog': 0xeaa,
    'Hangul_RieulMieum': 0xeab,
    'Hangul_RieulPieub': 0xeac,
    'Hangul_RieulSios': 0xead,
    'Hangul_RieulTieut': 0xeae,
    'Hangul_RieulPhieuf': 0xeaf,
    'Hangul_RieulHieuh': 0xeb0,
    'Hangul_Mieum': 0xeb1,
    'Hangul_Pieub': 0xeb2,
    'Hangul_SsangPieub': 0xeb3,
    'Hangul_PieubSios': 0xeb4,
    'Hangul_Sios': 0xeb5,
    'Hangul_SsangSios': 0xeb6,
    'Hangul_Ieung': 0xeb7,
    'Hangul_Jieuj': 0xeb8,
    'Hangul_SsangJieuj': 0xeb9,
    'Hangul_Cieuc': 0xeba,
    'Hangul_Khieuq': 0xebb,
    'Hangul_Tieut': 0xebc,
    'Hangul_Phieuf': 0xebd,
    'Hangul_Hieuh': 0xebe,
    'Hangul_A': 0xebf,
    'Hangul_AE': 0xec0,
    'Hangul_YA': 0xec1,
    'Hangul_YAE': 0xec2,
    'Hangul_EO': 0xec3,
    'Hangul_E': 0xec4,
    'Hangul_YEO': 0xec5,
    'Hangul_YE': 0xec6,
    'Hangul_O': 0xec7,
    'Hangul_WA': 0xec8,
    'Hangul_WAE': 0xec9,
    'Hangul_OE': 0xeca,
    'Hangul_YO': 0xecb,
    'Hangul_U': 0xecc,
    'Hangul_WEO': 0xecd,
    'Hangul_WE': 0xece,
    'Hangul_WI': 0xecf,
    'Hangul_YU': 0xed0,
    'Hangul_EU': 0xed1,
    'Hangul_YI': 0xed2,
    'Hangul_I': 0xed3,
    'Hangul_J_Kiyeog': 0xed4,
    'Hangul_J_SsangKiyeog': 0xed5,
    'Hangul_J_KiyeogSios': 0xed6,
    'Hangul_J_Nieun': 0xed7,
    'Hangul_J_NieunJieuj': 0xed8,
    'Hangul_J_NieunHieuh': 0xed9,
    'Hangul_J_Dikeud': 0xeda,
    'Hangul_J_Rieul': 0xedb,
    'Hangul_J_RieulKiyeog': 0xedc,
    'Hangul_J_RieulMieum': 0xedd,
    'Hangul_J_RieulPieub': 0xede,
    'Hangul_J_RieulSios': 0xedf,
    'Hangul_J_RieulTieut': 0xee0,
    'Hangul_J_RieulPhieuf': 0xee1,
    'Hangul_J_RieulHieuh': 0xee2,
    'Hangul_J_Mieum': 0xee3,
    'Hangul_J_Pieub': 0xee4,
    'Hangul_J_PieubSios': 0xee5,
    'Hangul_J_Sios': 0xee6,
    'Hangul_J_SsangSios': 0xee7,
    'Hangul_J_Ieung': 0xee8,
    'Hangul_J_Jieuj': 0xee9,
    'Hangul_J_Cieuc': 0xeea,
    'Hangul_J_Khieuq': 0xeeb,
    'Hangul_J_Tieut': 0xeec,
    'Hangul_J_Phieuf': 0xeed,
    'Hangul_J_Hieuh': 0xeee,
    'Hangul_RieulYeorinHieuh': 0xeef,
    'Hangul_SunkyeongeumMieum': 0xef0,
    'Hangul_SunkyeongeumPieub': 0xef1,
    'Hangul_PanSios': 0xef2,
    'Hangul_KkogjiDalrinIeung': 0xef3,
    'Hangul_SunkyeongeumPhieuf': 0xef4,
    'Hangul_YeorinHieuh': 0xef5,
    'Hangul_AraeA': 0xef6,
    'Hangul_AraeAE': 0xef7,
    'Hangul_J_PanSios': 0xef8,
    'Hangul_J_KkogjiDalrinIeung': 0xef9,
    'Hangul_J_YeorinHieuh': 0xefa,
    'Korean_Won': 0xeff,
    'OE': 0x13bc,
    'oe': 0x13bd,
    'Ydiaeresis': 0x13be,
    'EuroSign': 0x20ac,
    '3270_Duplicate': 0xfd01,
    '3270_FieldMark': 0xfd02,
    '3270_Right2': 0xfd03,
    '3270_Left2': 0xfd04,
    '3270_BackTab': 0xfd05,
    '3270_EraseEOF': 0xfd06,
    '3270_EraseInput': 0xfd07,
    '3270_Reset': 0xfd08,
    '3270_Quit': 0xfd09,
    '3270_PA1': 0xfd0a,
    '3270_PA2': 0xfd0b,
    '3270_PA3': 0xfd0c,
    '3270_Test': 0xfd0d,
    '3270_Attn': 0xfd0e,
    '3270_CursorBlink': 0xfd0f,
    '3270_AltCursor': 0xfd10,
    '3270_KeyClick': 0xfd11,
    '3270_Jump': 0xfd12,
    '3270_Ident': 0xfd13,
    '3270_Rule': 0xfd14,
    '3270_Copy': 0xfd15,
    '3270_Play': 0xfd16,
    '3270_Setup': 0xfd17,
    '3270_Record': 0xfd18,
    '3270_ChangeScreen': 0xfd19,
    '3270_DeleteWord': 0xfd1a,
    '3270_ExSelect': 0xfd1b,
    '3270_CursorSelect': 0xfd1c,
    '3270_PrintScreen': 0xfd1d,
    '3270_Enter': 0xfd1e,
    'ISO_Lock': 0xfe01,
    'ISO_Level2_Latch': 0xfe02,
    'ISO_Level3_Shift': 0xfe03,
    'ISO_Level3_Latch': 0xfe04,
    'ISO_Level3_Lock': 0xfe05,
    'ISO_Group_Latch': 0xfe06,
    'ISO_Group_Lock': 0xfe07,
    'ISO_Next_Group': 0xfe08,
    'ISO_Next_Group_Lock': 0xfe09,
    'ISO_Prev_Group': 0xfe0a,
    'ISO_Prev_Group_Lock': 0xfe0b,
    'ISO_First_Group': 0xfe0c,
    'ISO_First_Group_Lock': 0xfe0d,
    'ISO_Last_Group': 0xfe0e,
    'ISO_Last_Group_Lock': 0xfe0f,
    'ISO_Level5_Shift': 0xfe11,
    'ISO_Level5_Latch': 0xfe12,
    'ISO_Level5_Lock': 0xfe13,
    'ISO_Left_Tab': 0xfe20,
    'ISO_Move_Line_Up': 0xfe21,
    'ISO_Move_Line_Down': 0xfe22,
    'ISO_Partial_Line_Up': 0xfe23,
    'ISO_Partial_Line_Down': 0xfe24,
    'ISO_Partial_Space_Left': 0xfe25,
    'ISO_Partial_Space_Right': 0xfe26,
    'ISO_Set_Margin_Left': 0xfe27,
    'ISO_Set_Margin_Right': 0xfe28,
    'ISO_Release_Margin_Left': 0xfe29,
    'ISO_Release_Margin_Right': 0xfe2a,
    'ISO_Release_Both_Margins': 0xfe2b,
    'ISO_Fast_Cursor_Left': 0xfe2c,
    'ISO_Fast_Cursor_Right': 0xfe2d,
    'ISO_Fast_Cursor_Up': 0xfe2e,
    'ISO_Fast_Cursor_Down': 0xfe2f,
    'ISO_Continuous_Underline': 0xfe30,
    'ISO_Discontinuous_Underline': 0xfe31,
    'ISO_Emphasize': 0xfe32,
    'ISO_Center_Object': 0xfe33,
    'ISO_Enter': 0xfe34,
    'dead_grave': 0xfe50,
    'dead_acute': 0xfe51,
    'dead_circumflex': 0xfe52,
    'dead_tilde': 0xfe53,
    'dead_macron': 0xfe54,
    'dead_breve': 0xfe55,
    'dead_abovedot': 0xfe56,
    'dead_diaeresis': 0xfe57,
    'dead_abovering': 0xfe58,
    'dead_doubleacute': 0xfe59,
    'dead_caron': 0xfe5a,
    'dead_cedilla': 0xfe5b,
    'dead_ogonek': 0xfe5c,
    'dead_iota': 0xfe5d,
    'dead_voiced_sound': 0xfe5e,
    'dead_semivoiced_sound': 0xfe5f,
    'dead_belowdot': 0xfe60,
    'dead_hook': 0xfe61,
    'dead_horn': 0xfe62,
    'dead_stroke': 0xfe63,
    'dead_abovecomma': 0xfe64,
    'dead_abovereversedcomma': 0xfe65,
    'dead_doublegrave': 0xfe66,
    'dead_belowring': 0xfe67,
    'dead_belowmacron': 0xfe68,
    'dead_belowcircumflex': 0xfe69,
    'dead_belowtilde': 0xfe6a,
    'dead_belowbreve': 0xfe6b,
    'dead_belowdiaeresis': 0xfe6c,
    'dead_invertedbreve': 0xfe6d,
    'dead_belowcomma': 0xfe6e,
    'dead_currency': 0xfe6f,
    'AccessX_Enable': 0xfe70,
    'AccessX_Feedback_Enable': 0xfe71,
    'RepeatKeys_Enable': 0xfe72,
    'SlowKeys_Enable': 0xfe73,
    'BounceKeys_Enable': 0xfe74,
    'StickyKeys_Enable': 0xfe75,
    'MouseKeys_Enable': 0xfe76,
    'MouseKeys_Accel_Enable': 0xfe77,
    'Overlay1_Enable': 0xfe78,
    'Overlay2_Enable': 0xfe79,
    'AudibleBell_Enable': 0xfe7a,
    'dead_a': 0xfe80,
    'dead_A': 0xfe81,
    'dead_e': 0xfe82,
    'dead_E': 0xfe83,
    'dead_i': 0xfe84,
    'dead_I': 0xfe85,
    'dead_o': 0xfe86,
    'dead_O': 0xfe87,
    'dead_u': 0xfe88,
    'dead_U': 0xfe89,
    'dead_small_schwa': 0xfe8a,
    'dead_capital_schwa': 0xfe8b,
    'dead_greek': 0xfe8c,
    'ch': 0xfea0,
    'Ch': 0xfea1,
    'CH': 0xfea2,
    'c_h': 0xfea3,
    'C_h': 0xfea4,
    'C_H': 0xfea5,
    'First_Virtual_Screen': 0xfed0,
    'Prev_Virtual_Screen': 0xfed1,
    'Next_Virtual_Screen': 0xfed2,
    'Last_Virtual_Screen': 0xfed4,
    'Terminate_Server': 0xfed5,
    'Pointer_Left': 0xfee0,
    'Pointer_Right': 0xfee1,
    'Pointer_Up': 0xfee2,
    'Pointer_Down': 0xfee3,
    'Pointer_UpLeft': 0xfee4,
    'Pointer_UpRight': 0xfee5,
    'Pointer_DownLeft': 0xfee6,
    'Pointer_DownRight': 0xfee7,
    'Pointer_Button_Dflt': 0xfee8,
    'Pointer_Button1': 0xfee9,
    'Pointer_Button2': 0xfeea,
    'Pointer_Button3': 0xfeeb,
    'Pointer_Button4': 0xfeec,
    'Pointer_Button5': 0xfeed,
    'Pointer_DblClick_Dflt': 0xfeee,
    'Pointer_DblClick1': 0xfeef,
    'Pointer_DblClick2': 0xfef0,
    'Pointer_DblClick3': 0xfef1,
    'Pointer_DblClick4': 0xfef2,
    'Pointer_DblClick5': 0xfef3,
    'Pointer_Drag_Dflt': 0xfef4,
    'Pointer_Drag1': 0xfef5,
    'Pointer_Drag2': 0xfef6,
    'Pointer_Drag3': 0xfef7,
    'Pointer_Drag4': 0xfef8,
    'Pointer_EnableKeys': 0xfef9,
    'Pointer_Accelerate': 0xfefa,
    'Pointer_DfltBtnNext': 0xfefb,
    'Pointer_DfltBtnPrev': 0xfefc,
    'Pointer_Drag5': 0xfefd,
    'BackSpace': 0xff08,
    'Tab': 0xff09,
    'Linefeed': 0xff0a,
    'Clear': 0xff0b,
    'Return': 0xff0d,
    'Pause': 0xff13,
    'Scroll_Lock': 0xff14,
    'Sys_Req': 0xff15,
    'Escape': 0xff1b,
    'Multi_key': 0xff20,
    'Kanji': 0xff21,
    'Muhenkan': 0xff22,
    'Henkan': 0xff23,
    'Romaji': 0xff24,
    'Hiragana': 0xff25,
    'Katakana': 0xff26,
    'Hiragana_Katakana': 0xff27,
    'Zenkaku': 0xff28,
    'Hankaku': 0xff29,
    'Zenkaku_Hankaku': 0xff2a,
    'Touroku': 0xff2b,
    'Massyo': 0xff2c,
    'Kana_Lock': 0xff2d,
    'Kana_Shift': 0xff2e,
    'Eisu_Shift': 0xff2f,
    'Eisu_toggle': 0xff30,
    'Hangul': 0xff31,
    'Hangul_Start': 0xff32,
    'Hangul_End': 0xff33,
    'Hangul_Hanja': 0xff34,
    'Hangul_Jamo': 0xff35,
    'Hangul_Romaja': 0xff36,
    'Hangul_Codeinput': 0xff37,
    'Hangul_Jeonja': 0xff38,
    'Hangul_Banja': 0xff39,
    'Hangul_PreHanja': 0xff3a,
    'Hangul_PostHanja': 0xff3b,
    'Hangul_SingleCandidate': 0xff3c,
    'Hangul_MultipleCandidate': 0xff3d,
    'Hangul_PreviousCandidate': 0xff3e,
    'Hangul_Special': 0xff3f,
    'Home': 0xff50,
    'Left': 0xff51,
    'Up': 0xff52,
    'Right': 0xff53,
    'Down': 0xff54,
    'Prior': 0xff55,
    'Next': 0xff56,
    'End': 0xff57,
    'Begin': 0xff58,
    'Select': 0xff60,
    'Print': 0xff61,
    'Execute': 0xff62,
    'Insert': 0xff63,
    'Undo': 0xff65,
    'Redo': 0xff66,
    'Menu': 0xff67,
    'Find': 0xff68,
    'Cancel': 0xff69,
    'Help': 0xff6a,
    'Break': 0xff6b,
    'Arabic_switch': 0xff7e,
    'Num_Lock': 0xff7f,
    'KP_Space': 0xff80,
    'KP_Tab': 0xff89,
    'KP_Enter': 0xff8d,
    'KP_F1': 0xff91,
    'KP_F2': 0xff92,
    'KP_F3': 0xff93,
    'KP_F4': 0xff94,
    'KP_Home': 0xff95,
    'KP_Left': 0xff96,
    'KP_Up': 0xff97,
    'KP_Right': 0xff98,
    'KP_Down': 0xff99,
    'KP_Prior': 0xff9a,
    'KP_Next': 0xff9b,
    'KP_End': 0xff9c,
    'KP_Begin': 0xff9d,
    'KP_Insert': 0xff9e,
    'KP_Delete': 0xff9f,
    'KP_Multiply': 0xffaa,
    'KP_Add': 0xffab,
    'KP_Separator': 0xffac,
    'KP_Subtract': 0xffad,
    'KP_Decimal': 0xffae,
    'KP_Divide': 0xffaf,
    'KP_0': 0xffb0,
    'KP_1': 0xffb1,
    'KP_2': 0xffb2,
    'KP_3': 0xffb3,
    'KP_4': 0xffb4,
    'KP_5': 0xffb5,
    'KP_6': 0xffb6,
    'KP_7': 0xffb7,
    'KP_8': 0xffb8,
    'KP_9': 0xffb9,
    'KP_Equal': 0xffbd,
    'F1': 0xffbe,
    'F2': 0xffbf,
    'F3': 0xffc0,
    'F4': 0xffc1,
    'F5': 0xffc2,
    'F6': 0xffc3,
    'F7': 0xffc4,
    'F8': 0xffc5,
    'F9': 0xffc6,
    'F10': 0xffc7,
    'F11': 0xffc8,
    'L1': 0xffc8,
    'F12': 0xffc9,
    'L2': 0xffc9,
    'F13': 0xffca,
    'L3': 0xffca,
    'F14': 0xffcb,
    'L4': 0xffcb,
    'F15': 0xffcc,
    'L5': 0xffcc,
    'F16': 0xffcd,
    'L6': 0xffcd,
    'F17': 0xffce,
    'L7': 0xffce,
    'F18': 0xffcf,
    'L8': 0xffcf,
    'F19': 0xffd0,
    'L9': 0xffd0,
    'F20': 0xffd1,
    'L10': 0xffd1,
    'F21': 0xffd2,
    'R1': 0xffd2,
    'F22': 0xffd3,
    'R2': 0xffd3,
    'F23': 0xffd4,
    'R3': 0xffd4,
    'F24': 0xffd5,
    'R4': 0xffd5,
    'F25': 0xffd6,
    'R5': 0xffd6,
    'F26': 0xffd7,
    'R6': 0xffd7,
    'F27': 0xffd8,
    'R7': 0xffd8,
    'F28': 0xffd9,
    'R8': 0xffd9,
    'F29': 0xffda,
    'R9': 0xffda,
    'F30': 0xffdb,
    'R10': 0xffdb,
    'F31': 0xffdc,
    'R11': 0xffdc,
    'F32': 0xffdd,
    'R12': 0xffdd,
    'F33': 0xffde,
    'R13': 0xffde,
    'F34': 0xffdf,
    'R14': 0xffdf,
    'F35': 0xffe0,
    'R15': 0xffe0,
    'Shift_L': 0xffe1,
    'Shift_R': 0xffe2,
    'Control_L': 0xffe3,
    'Control_R': 0xffe4,
    'Caps_Lock': 0xffe5,
    'Shift_Lock': 0xffe6,
    'Meta_L': 0xffe7,
    'Meta_R': 0xffe8,
    'Alt_L': 0xffe9,
    'Alt_R': 0xffea,
    'Super_L': 0xffeb,
    'Super_R': 0xffec,
    'Hyper_L': 0xffed,
    'Hyper_R': 0xffee,
    'braille_dot_1': 0xfff1,
    'braille_dot_2': 0xfff2,
    'braille_dot_3': 0xfff3,
    'braille_dot_4': 0xfff4,
    'braille_dot_5': 0xfff5,
    'braille_dot_6': 0xfff6,
    'braille_dot_7': 0xfff7,
    'braille_dot_8': 0xfff8,
    'braille_dot_9': 0xfff9,
    'braille_dot_10': 0xfffa,
    'Delete': 0xffff,
    'VoidSymbol': 0xffffff,
    'Ibreve': 0x100012c,
    'ibreve': 0x100012d,
    'Wcircumflex': 0x1000174,
    'wcircumflex': 0x1000175,
    'Ycircumflex': 0x1000176,
    'ycircumflex': 0x1000177,
    'SCHWA': 0x100018f,
    'Obarred': 0x100019f,
    'Ohorn': 0x10001a0,
    'ohorn': 0x10001a1,
    'Uhorn': 0x10001af,
    'uhorn': 0x10001b0,
    'Zstroke': 0x10001b5,
    'zstroke': 0x10001b6,
    'EZH': 0x10001b7,
    'Ocaron': 0x10001d1,
    'ocaron': 0x10001d2,
    'Gcaron': 0x10001e6,
    'gcaron': 0x10001e7,
    'schwa': 0x1000259,
    'obarred': 0x1000275,
    'ezh': 0x1000292,
    'Cyrillic_GHE_bar': 0x1000492,
    'Cyrillic_ghe_bar': 0x1000493,
    'Cyrillic_ZHE_descender': 0x1000496,
    'Cyrillic_zhe_descender': 0x1000497,
    'Cyrillic_KA_descender': 0x100049a,
    'Cyrillic_ka_descender': 0x100049b,
    'Cyrillic_KA_vertstroke': 0x100049c,
    'Cyrillic_ka_vertstroke': 0x100049d,
    'Cyrillic_EN_descender': 0x10004a2,
    'Cyrillic_en_descender': 0x10004a3,
    'Cyrillic_U_straight': 0x10004ae,
    'Cyrillic_u_straight': 0x10004af,
    'Cyrillic_U_straight_bar': 0x10004b0,
    'Cyrillic_u_straight_bar': 0x10004b1,
    'Cyrillic_HA_descender': 0x10004b2,
    'Cyrillic_ha_descender': 0x10004b3,
    'Cyrillic_CHE_descender': 0x10004b6,
    'Cyrillic_che_descender': 0x10004b7,
    'Cyrillic_CHE_vertstroke': 0x10004b8,
    'Cyrillic_che_vertstroke': 0x10004b9,
    'Cyrillic_SHHA': 0x10004ba,
    'Cyrillic_shha': 0x10004bb,
    'Cyrillic_SCHWA': 0x10004d8,
    'Cyrillic_schwa': 0x10004d9,
    'Cyrillic_I_macron': 0x10004e2,
    'Cyrillic_i_macron': 0x10004e3,
    'Cyrillic_O_bar': 0x10004e8,
    'Cyrillic_o_bar': 0x10004e9,
    'Cyrillic_U_macron': 0x10004ee,
    'Cyrillic_u_macron': 0x10004ef,
    'Armenian_AYB': 0x1000531,
    'Armenian_BEN': 0x1000532,
    'Armenian_GIM': 0x1000533,
    'Armenian_DA': 0x1000534,
    'Armenian_YECH': 0x1000535,
    'Armenian_ZA': 0x1000536,
    'Armenian_E': 0x1000537,
    'Armenian_AT': 0x1000538,
    'Armenian_TO': 0x1000539,
    'Armenian_ZHE': 0x100053a,
    'Armenian_INI': 0x100053b,
    'Armenian_LYUN': 0x100053c,
    'Armenian_KHE': 0x100053d,
    'Armenian_TSA': 0x100053e,
    'Armenian_KEN': 0x100053f,
    'Armenian_HO': 0x1000540,
    'Armenian_DZA': 0x1000541,
    'Armenian_GHAT': 0x1000542,
    'Armenian_TCHE': 0x1000543,
    'Armenian_MEN': 0x1000544,
    'Armenian_HI': 0x1000545,
    'Armenian_NU': 0x1000546,
    'Armenian_SHA': 0x1000547,
    'Armenian_VO': 0x1000548,
    'Armenian_CHA': 0x1000549,
    'Armenian_PE': 0x100054a,
    'Armenian_JE': 0x100054b,
    'Armenian_RA': 0x100054c,
    'Armenian_SE': 0x100054d,
    'Armenian_VEV': 0x100054e,
    'Armenian_TYUN': 0x100054f,
    'Armenian_RE': 0x1000550,
    'Armenian_TSO': 0x1000551,
    'Armenian_VYUN': 0x1000552,
    'Armenian_PYUR': 0x1000553,
    'Armenian_KE': 0x1000554,
    'Armenian_O': 0x1000555,
    'Armenian_FE': 0x1000556,
    'Armenian_apostrophe': 0x100055a,
    'Armenian_accent': 0x100055b,
    'Armenian_amanak': 0x100055c,
    'Armenian_separation_mark': 0x100055d,
    'Armenian_question': 0x100055e,
    'Armenian_ayb': 0x1000561,
    'Armenian_ben': 0x1000562,
    'Armenian_gim': 0x1000563,
    'Armenian_da': 0x1000564,
    'Armenian_yech': 0x1000565,
    'Armenian_za': 0x1000566,
    'Armenian_e': 0x1000567,
    'Armenian_at': 0x1000568,
    'Armenian_to': 0x1000569,
    'Armenian_zhe': 0x100056a,
    'Armenian_ini': 0x100056b,
    'Armenian_lyun': 0x100056c,
    'Armenian_khe': 0x100056d,
    'Armenian_tsa': 0x100056e,
    'Armenian_ken': 0x100056f,
    'Armenian_ho': 0x1000570,
    'Armenian_dza': 0x1000571,
    'Armenian_ghat': 0x1000572,
    'Armenian_tche': 0x1000573,
    'Armenian_men': 0x1000574,
    'Armenian_hi': 0x1000575,
    'Armenian_nu': 0x1000576,
    'Armenian_sha': 0x1000577,
    'Armenian_vo': 0x1000578,
    'Armenian_cha': 0x1000579,
    'Armenian_pe': 0x100057a,
    'Armenian_je': 0x100057b,
    'Armenian_ra': 0x100057c,
    'Armenian_se': 0x100057d,
    'Armenian_vev': 0x100057e,
    'Armenian_tyun': 0x100057f,
    'Armenian_re': 0x1000580,
    'Armenian_tso': 0x1000581,
    'Armenian_vyun': 0x1000582,
    'Armenian_pyur': 0x1000583,
    'Armenian_ke': 0x1000584,
    'Armenian_o': 0x1000585,
    'Armenian_fe': 0x1000586,
    'Armenian_ligature_ew': 0x1000587,
    'Armenian_full_stop': 0x1000589,
    'Armenian_yentamna': 0x100058a,
    'Arabic_madda_above': 0x1000653,
    'Arabic_hamza_above': 0x1000654,
    'Arabic_hamza_below': 0x1000655,
    'Arabic_0': 0x1000660,
    'Arabic_1': 0x1000661,
    'Arabic_2': 0x1000662,
    'Arabic_3': 0x1000663,
    'Arabic_4': 0x1000664,
    'Arabic_5': 0x1000665,
    'Arabic_6': 0x1000666,
    'Arabic_7': 0x1000667,
    'Arabic_8': 0x1000668,
    'Arabic_9': 0x1000669,
    'Arabic_percent': 0x100066a,
    'Arabic_superscript_alef': 0x1000670,
    'Arabic_tteh': 0x1000679,
    'Arabic_peh': 0x100067e,
    'Arabic_tcheh': 0x1000686,
    'Arabic_ddal': 0x1000688,
    'Arabic_rreh': 0x1000691,
    'Arabic_jeh': 0x1000698,
    'Arabic_veh': 0x10006a4,
    'Arabic_keheh': 0x10006a9,
    'Arabic_gaf': 0x10006af,
    'Arabic_noon_ghunna': 0x10006ba,
    'Arabic_heh_doachashmee': 0x10006be,
    'Arabic_heh_goal': 0x10006c1,
    'Farsi_yeh': 0x10006cc,
    'Arabic_yeh_baree': 0x10006d2,
    'Arabic_fullstop': 0x10006d4,
    'Farsi_0': 0x10006f0,
    'Farsi_1': 0x10006f1,
    'Farsi_2': 0x10006f2,
    'Farsi_3': 0x10006f3,
    'Farsi_4': 0x10006f4,
    'Farsi_5': 0x10006f5,
    'Farsi_6': 0x10006f6,
    'Farsi_7': 0x10006f7,
    'Farsi_8': 0x10006f8,
    'Farsi_9': 0x10006f9,
    'Sinh_ng': 0x1000d82,
    'Sinh_h2': 0x1000d83,
    'Sinh_a': 0x1000d85,
    'Sinh_aa': 0x1000d86,
    'Sinh_ae': 0x1000d87,
    'Sinh_aee': 0x1000d88,
    'Sinh_i': 0x1000d89,
    'Sinh_ii': 0x1000d8a,
    'Sinh_u': 0x1000d8b,
    'Sinh_uu': 0x1000d8c,
    'Sinh_ri': 0x1000d8d,
    'Sinh_rii': 0x1000d8e,
    'Sinh_lu': 0x1000d8f,
    'Sinh_luu': 0x1000d90,
    'Sinh_e': 0x1000d91,
    'Sinh_ee': 0x1000d92,
    'Sinh_ai': 0x1000d93,
    'Sinh_o': 0x1000d94,
    'Sinh_oo': 0x1000d95,
    'Sinh_au': 0x1000d96,
    'Sinh_ka': 0x1000d9a,
    'Sinh_kha': 0x1000d9b,
    'Sinh_ga': 0x1000d9c,
    'Sinh_gha': 0x1000d9d,
    'Sinh_ng2': 0x1000d9e,
    'Sinh_nga': 0x1000d9f,
    'Sinh_ca': 0x1000da0,
    'Sinh_cha': 0x1000da1,
    'Sinh_ja': 0x1000da2,
    'Sinh_jha': 0x1000da3,
    'Sinh_nya': 0x1000da4,
    'Sinh_jnya': 0x1000da5,
    'Sinh_nja': 0x1000da6,
    'Sinh_tta': 0x1000da7,
    'Sinh_ttha': 0x1000da8,
    'Sinh_dda': 0x1000da9,
    'Sinh_ddha': 0x1000daa,
    'Sinh_nna': 0x1000dab,
    'Sinh_ndda': 0x1000dac,
    'Sinh_tha': 0x1000dad,
    'Sinh_thha': 0x1000dae,
    'Sinh_dha': 0x1000daf,
    'Sinh_dhha': 0x1000db0,
    'Sinh_na': 0x1000db1,
    'Sinh_ndha': 0x1000db3,
    'Sinh_pa': 0x1000db4,
    'Sinh_pha': 0x1000db5,
    'Sinh_ba': 0x1000db6,
    'Sinh_bha': 0x1000db7,
    'Sinh_ma': 0x1000db8,
    'Sinh_mba': 0x1000db9,
    'Sinh_ya': 0x1000dba,
    'Sinh_ra': 0x1000dbb,
    'Sinh_la': 0x1000dbd,
    'Sinh_va': 0x1000dc0,
    'Sinh_sha': 0x1000dc1,
    'Sinh_ssha': 0x1000dc2,
    'Sinh_sa': 0x1000dc3,
    'Sinh_ha': 0x1000dc4,
    'Sinh_lla': 0x1000dc5,
    'Sinh_fa': 0x1000dc6,
    'Sinh_al': 0x1000dca,
    'Sinh_aa2': 0x1000dcf,
    'Sinh_ae2': 0x1000dd0,
    'Sinh_aee2': 0x1000dd1,
    'Sinh_i2': 0x1000dd2,
    'Sinh_ii2': 0x1000dd3,
    'Sinh_u2': 0x1000dd4,
    'Sinh_uu2': 0x1000dd6,
    'Sinh_ru2': 0x1000dd8,
    'Sinh_e2': 0x1000dd9,
    'Sinh_ee2': 0x1000dda,
    'Sinh_ai2': 0x1000ddb,
    'Sinh_o2': 0x1000ddc,
    'Sinh_oo2': 0x1000ddd,
    'Sinh_au2': 0x1000dde,
    'Sinh_lu2': 0x1000ddf,
    'Sinh_ruu2': 0x1000df2,
    'Sinh_luu2': 0x1000df3,
    'Sinh_kunddaliya': 0x1000df4,
    'Georgian_an': 0x10010d0,
    'Georgian_ban': 0x10010d1,
    'Georgian_gan': 0x10010d2,
    'Georgian_don': 0x10010d3,
    'Georgian_en': 0x10010d4,
    'Georgian_vin': 0x10010d5,
    'Georgian_zen': 0x10010d6,
    'Georgian_tan': 0x10010d7,
    'Georgian_in': 0x10010d8,
    'Georgian_kan': 0x10010d9,
    'Georgian_las': 0x10010da,
    'Georgian_man': 0x10010db,
    'Georgian_nar': 0x10010dc,
    'Georgian_on': 0x10010dd,
    'Georgian_par': 0x10010de,
    'Georgian_zhar': 0x10010df,
    'Georgian_rae': 0x10010e0,
    'Georgian_san': 0x10010e1,
    'Georgian_tar': 0x10010e2,
    'Georgian_un': 0x10010e3,
    'Georgian_phar': 0x10010e4,
    'Georgian_khar': 0x10010e5,
    'Georgian_ghan': 0x10010e6,
    'Georgian_qar': 0x10010e7,
    'Georgian_shin': 0x10010e8,
    'Georgian_chin': 0x10010e9,
    'Georgian_can': 0x10010ea,
    'Georgian_jil': 0x10010eb,
    'Georgian_cil': 0x10010ec,
    'Georgian_char': 0x10010ed,
    'Georgian_xan': 0x10010ee,
    'Georgian_jhan': 0x10010ef,
    'Georgian_hae': 0x10010f0,
    'Georgian_he': 0x10010f1,
    'Georgian_hie': 0x10010f2,
    'Georgian_we': 0x10010f3,
    'Georgian_har': 0x10010f4,
    'Georgian_hoe': 0x10010f5,
    'Georgian_fi': 0x10010f6,
    'Babovedot': 0x1001e02,
    'babovedot': 0x1001e03,
    'Dabovedot': 0x1001e0a,
    'dabovedot': 0x1001e0b,
    'Fabovedot': 0x1001e1e,
    'fabovedot': 0x1001e1f,
    'Lbelowdot': 0x1001e36,
    'lbelowdot': 0x1001e37,
    'Mabovedot': 0x1001e40,
    'mabovedot': 0x1001e41,
    'Pabovedot': 0x1001e56,
    'pabovedot': 0x1001e57,
    'Sabovedot': 0x1001e60,
    'sabovedot': 0x1001e61,
    'Tabovedot': 0x1001e6a,
    'tabovedot': 0x1001e6b,
    'Wgrave': 0x1001e80,
    'wgrave': 0x1001e81,
    'Wacute': 0x1001e82,
    'wacute': 0x1001e83,
    'Wdiaeresis': 0x1001e84,
    'wdiaeresis': 0x1001e85,
    'Xabovedot': 0x1001e8a,
    'xabovedot': 0x1001e8b,
    'Abelowdot': 0x1001ea0,
    'abelowdot': 0x1001ea1,
    'Ahook': 0x1001ea2,
    'ahook': 0x1001ea3,
    'Acircumflexacute': 0x1001ea4,
    'acircumflexacute': 0x1001ea5,
    'Acircumflexgrave': 0x1001ea6,
    'acircumflexgrave': 0x1001ea7,
    'Acircumflexhook': 0x1001ea8,
    'acircumflexhook': 0x1001ea9,
    'Acircumflextilde': 0x1001eaa,
    'acircumflextilde': 0x1001eab,
    'Acircumflexbelowdot': 0x1001eac,
    'acircumflexbelowdot': 0x1001ead,
    'Abreveacute': 0x1001eae,
    'abreveacute': 0x1001eaf,
    'Abrevegrave': 0x1001eb0,
    'abrevegrave': 0x1001eb1,
    'Abrevehook': 0x1001eb2,
    'abrevehook': 0x1001eb3,
    'Abrevetilde': 0x1001eb4,
    'abrevetilde': 0x1001eb5,
    'Abrevebelowdot': 0x1001eb6,
    'abrevebelowdot': 0x1001eb7,
    'Ebelowdot': 0x1001eb8,
    'ebelowdot': 0x1001eb9,
    'Ehook': 0x1001eba,
    'ehook': 0x1001ebb,
    'Etilde': 0x1001ebc,
    'etilde': 0x1001ebd,
    'Ecircumflexacute': 0x1001ebe,
    'ecircumflexacute': 0x1001ebf,
    'Ecircumflexgrave': 0x1001ec0,
    'ecircumflexgrave': 0x1001ec1,
    'Ecircumflexhook': 0x1001ec2,
    'ecircumflexhook': 0x1001ec3,
    'Ecircumflextilde': 0x1001ec4,
    'ecircumflextilde': 0x1001ec5,
    'Ecircumflexbelowdot': 0x1001ec6,
    'ecircumflexbelowdot': 0x1001ec7,
    'Ihook': 0x1001ec8,
    'ihook': 0x1001ec9,
    'Ibelowdot': 0x1001eca,
    'ibelowdot': 0x1001ecb,
    'Obelowdot': 0x1001ecc,
    'obelowdot': 0x1001ecd,
    'Ohook': 0x1001ece,
    'ohook': 0x1001ecf,
    'Ocircumflexacute': 0x1001ed0,
    'ocircumflexacute': 0x1001ed1,
    'Ocircumflexgrave': 0x1001ed2,
    'ocircumflexgrave': 0x1001ed3,
    'Ocircumflexhook': 0x1001ed4,
    'ocircumflexhook': 0x1001ed5,
    'Ocircumflextilde': 0x1001ed6,
    'ocircumflextilde': 0x1001ed7,
    'Ocircumflexbelowdot': 0x1001ed8,
    'ocircumflexbelowdot': 0x1001ed9,
    'Ohornacute': 0x1001eda,
    'ohornacute': 0x1001edb,
    'Ohorngrave': 0x1001edc,
    'ohorngrave': 0x1001edd,
    'Ohornhook': 0x1001ede,
    'ohornhook': 0x1001edf,
    'Ohorntilde': 0x1001ee0,
    'ohorntilde': 0x1001ee1,
    'Ohornbelowdot': 0x1001ee2,
    'ohornbelowdot': 0x1001ee3,
    'Ubelowdot': 0x1001ee4,
    'ubelowdot': 0x1001ee5,
    'Uhook': 0x1001ee6,
    'uhook': 0x1001ee7,
    'Uhornacute': 0x1001ee8,
    'uhornacute': 0x1001ee9,
    'Uhorngrave': 0x1001eea,
    'uhorngrave': 0x1001eeb,
    'Uhornhook': 0x1001eec,
    'uhornhook': 0x1001eed,
    'Uhorntilde': 0x1001eee,
    'uhorntilde': 0x1001eef,
    'Uhornbelowdot': 0x1001ef0,
    'uhornbelowdot': 0x1001ef1,
    'Ygrave': 0x1001ef2,
    'ygrave': 0x1001ef3,
    'Ybelowdot': 0x1001ef4,
    'ybelowdot': 0x1001ef5,
    'Yhook': 0x1001ef6,
    'yhook': 0x1001ef7,
    'Ytilde': 0x1001ef8,
    'ytilde': 0x1001ef9,
    'zerosuperior': 0x1002070,
    'foursuperior': 0x1002074,
    'fivesuperior': 0x1002075,
    'sixsuperior': 0x1002076,
    'sevensuperior': 0x1002077,
    'eightsuperior': 0x1002078,
    'ninesuperior': 0x1002079,
    'zerosubscript': 0x1002080,
    'onesubscript': 0x1002081,
    'twosubscript': 0x1002082,
    'threesubscript': 0x1002083,
    'foursubscript': 0x1002084,
    'fivesubscript': 0x1002085,
    'sixsubscript': 0x1002086,
    'sevensubscript': 0x1002087,
    'eightsubscript': 0x1002088,
    'ninesubscript': 0x1002089,
    'EcuSign': 0x10020a0,
    'ColonSign': 0x10020a1,
    'CruzeiroSign': 0x10020a2,
    'FFrancSign': 0x10020a3,
    'LiraSign': 0x10020a4,
    'MillSign': 0x10020a5,
    'NairaSign': 0x10020a6,
    'PesetaSign': 0x10020a7,
    'RupeeSign': 0x10020a8,
    'WonSign': 0x10020a9,
    'NewSheqelSign': 0x10020aa,
    'DongSign': 0x10020ab,
    'partdifferential': 0x1002202,
    'emptyset': 0x1002205,
    'elementof': 0x1002208,
    'notelementof': 0x1002209,
    'containsas': 0x100220b,
    'squareroot': 0x100221a,
    'cuberoot': 0x100221b,
    'fourthroot': 0x100221c,
    'dintegral': 0x100222c,
    'tintegral': 0x100222d,
    'because': 0x1002235,
    'notapproxeq': 0x1002247,
    'approxeq': 0x1002248,
    'notidentical': 0x1002262,
    'stricteq': 0x1002263,
    'braille_blank': 0x1002800,
    'braille_dots_1': 0x1002801,
    'braille_dots_2': 0x1002802,
    'braille_dots_12': 0x1002803,
    'braille_dots_3': 0x1002804,
    'braille_dots_13': 0x1002805,
    'braille_dots_23': 0x1002806,
    'braille_dots_123': 0x1002807,
    'braille_dots_4': 0x1002808,
    'braille_dots_14': 0x1002809,
    'braille_dots_24': 0x100280a,
    'braille_dots_124': 0x100280b,
    'braille_dots_34': 0x100280c,
    'braille_dots_134': 0x100280d,
    'braille_dots_234': 0x100280e,
    'braille_dots_1234': 0x100280f,
    'braille_dots_5': 0x1002810,
    'braille_dots_15': 0x1002811,
    'braille_dots_25': 0x1002812,
    'braille_dots_125': 0x1002813,
    'braille_dots_35': 0x1002814,
    'braille_dots_135': 0x1002815,
    'braille_dots_235': 0x1002816,
    'braille_dots_1235': 0x1002817,
    'braille_dots_45': 0x1002818,
    'braille_dots_145': 0x1002819,
    'braille_dots_245': 0x100281a,
    'braille_dots_1245': 0x100281b,
    'braille_dots_345': 0x100281c,
    'braille_dots_1345': 0x100281d,
    'braille_dots_2345': 0x100281e,
    'braille_dots_12345': 0x100281f,
    'braille_dots_6': 0x1002820,
    'braille_dots_16': 0x1002821,
    'braille_dots_26': 0x1002822,
    'braille_dots_126': 0x1002823,
    'braille_dots_36': 0x1002824,
    'braille_dots_136': 0x1002825,
    'braille_dots_236': 0x1002826,
    'braille_dots_1236': 0x1002827,
    'braille_dots_46': 0x1002828,
    'braille_dots_146': 0x1002829,
    'braille_dots_246': 0x100282a,
    'braille_dots_1246': 0x100282b,
    'braille_dots_346': 0x100282c,
    'braille_dots_1346': 0x100282d,
    'braille_dots_2346': 0x100282e,
    'braille_dots_12346': 0x100282f,
    'braille_dots_56': 0x1002830,
    'braille_dots_156': 0x1002831,
    'braille_dots_256': 0x1002832,
    'braille_dots_1256': 0x1002833,
    'braille_dots_356': 0x1002834,
    'braille_dots_1356': 0x1002835,
    'braille_dots_2356': 0x1002836,
    'braille_dots_12356': 0x1002837,
    'braille_dots_456': 0x1002838,
    'braille_dots_1456': 0x1002839,
    'braille_dots_2456': 0x100283a,
    'braille_dots_12456': 0x100283b,
    'braille_dots_3456': 0x100283c,
    'braille_dots_13456': 0x100283d,
    'braille_dots_23456': 0x100283e,
    'braille_dots_123456': 0x100283f,
    'braille_dots_7': 0x1002840,
    'braille_dots_17': 0x1002841,
    'braille_dots_27': 0x1002842,
    'braille_dots_127': 0x1002843,
    'braille_dots_37': 0x1002844,
    'braille_dots_137': 0x1002845,
    'braille_dots_237': 0x1002846,
    'braille_dots_1237': 0x1002847,
    'braille_dots_47': 0x1002848,
    'braille_dots_147': 0x1002849,
    'braille_dots_247': 0x100284a,
    'braille_dots_1247': 0x100284b,
    'braille_dots_347': 0x100284c,
    'braille_dots_1347': 0x100284d,
    'braille_dots_2347': 0x100284e,
    'braille_dots_12347': 0x100284f,
    'braille_dots_57': 0x1002850,
    'braille_dots_157': 0x1002851,
    'braille_dots_257': 0x1002852,
    'braille_dots_1257': 0x1002853,
    'braille_dots_357': 0x1002854,
    'braille_dots_1357': 0x1002855,
    'braille_dots_2357': 0x1002856,
    'braille_dots_12357': 0x1002857,
    'braille_dots_457': 0x1002858,
    'braille_dots_1457': 0x1002859,
    'braille_dots_2457': 0x100285a,
    'braille_dots_12457': 0x100285b,
    'braille_dots_3457': 0x100285c,
    'braille_dots_13457': 0x100285d,
    'braille_dots_23457': 0x100285e,
    'braille_dots_123457': 0x100285f,
    'braille_dots_67': 0x1002860,
    'braille_dots_167': 0x1002861,
    'braille_dots_267': 0x1002862,
    'braille_dots_1267': 0x1002863,
    'braille_dots_367': 0x1002864,
    'braille_dots_1367': 0x1002865,
    'braille_dots_2367': 0x1002866,
    'braille_dots_12367': 0x1002867,
    'braille_dots_467': 0x1002868,
    'braille_dots_1467': 0x1002869,
    'braille_dots_2467': 0x100286a,
    'braille_dots_12467': 0x100286b,
    'braille_dots_3467': 0x100286c,
    'braille_dots_13467': 0x100286d,
    'braille_dots_23467': 0x100286e,
    'braille_dots_123467': 0x100286f,
    'braille_dots_567': 0x1002870,
    'braille_dots_1567': 0x1002871,
    'braille_dots_2567': 0x1002872,
    'braille_dots_12567': 0x1002873,
    'braille_dots_3567': 0x1002874,
    'braille_dots_13567': 0x1002875,
    'braille_dots_23567': 0x1002876,
    'braille_dots_123567': 0x1002877,
    'braille_dots_4567': 0x1002878,
    'braille_dots_14567': 0x1002879,
    'braille_dots_24567': 0x100287a,
    'braille_dots_124567': 0x100287b,
    'braille_dots_34567': 0x100287c,
    'braille_dots_134567': 0x100287d,
    'braille_dots_234567': 0x100287e,
    'braille_dots_1234567': 0x100287f,
    'braille_dots_8': 0x1002880,
    'braille_dots_18': 0x1002881,
    'braille_dots_28': 0x1002882,
    'braille_dots_128': 0x1002883,
    'braille_dots_38': 0x1002884,
    'braille_dots_138': 0x1002885,
    'braille_dots_238': 0x1002886,
    'braille_dots_1238': 0x1002887,
    'braille_dots_48': 0x1002888,
    'braille_dots_148': 0x1002889,
    'braille_dots_248': 0x100288a,
    'braille_dots_1248': 0x100288b,
    'braille_dots_348': 0x100288c,
    'braille_dots_1348': 0x100288d,
    'braille_dots_2348': 0x100288e,
    'braille_dots_12348': 0x100288f,
    'braille_dots_58': 0x1002890,
    'braille_dots_158': 0x1002891,
    'braille_dots_258': 0x1002892,
    'braille_dots_1258': 0x1002893,
    'braille_dots_358': 0x1002894,
    'braille_dots_1358': 0x1002895,
    'braille_dots_2358': 0x1002896,
    'braille_dots_12358': 0x1002897,
    'braille_dots_458': 0x1002898,
    'braille_dots_1458': 0x1002899,
    'braille_dots_2458': 0x100289a,
    'braille_dots_12458': 0x100289b,
    'braille_dots_3458': 0x100289c,
    'braille_dots_13458': 0x100289d,
    'braille_dots_23458': 0x100289e,
    'braille_dots_123458': 0x100289f,
    'braille_dots_68': 0x10028a0,
    'braille_dots_168': 0x10028a1,
    'braille_dots_268': 0x10028a2,
    'braille_dots_1268': 0x10028a3,
    'braille_dots_368': 0x10028a4,
    'braille_dots_1368': 0x10028a5,
    'braille_dots_2368': 0x10028a6,
    'braille_dots_12368': 0x10028a7,
    'braille_dots_468': 0x10028a8,
    'braille_dots_1468': 0x10028a9,
    'braille_dots_2468': 0x10028aa,
    'braille_dots_12468': 0x10028ab,
    'braille_dots_3468': 0x10028ac,
    'braille_dots_13468': 0x10028ad,
    'braille_dots_23468': 0x10028ae,
    'braille_dots_123468': 0x10028af,
    'braille_dots_568': 0x10028b0,
    'braille_dots_1568': 0x10028b1,
    'braille_dots_2568': 0x10028b2,
    'braille_dots_12568': 0x10028b3,
    'braille_dots_3568': 0x10028b4,
    'braille_dots_13568': 0x10028b5,
    'braille_dots_23568': 0x10028b6,
    'braille_dots_123568': 0x10028b7,
    'braille_dots_4568': 0x10028b8,
    'braille_dots_14568': 0x10028b9,
    'braille_dots_24568': 0x10028ba,
    'braille_dots_124568': 0x10028bb,
    'braille_dots_34568': 0x10028bc,
    'braille_dots_134568': 0x10028bd,
    'braille_dots_234568': 0x10028be,
    'braille_dots_1234568': 0x10028bf,
    'braille_dots_78': 0x10028c0,
    'braille_dots_178': 0x10028c1,
    'braille_dots_278': 0x10028c2,
    'braille_dots_1278': 0x10028c3,
    'braille_dots_378': 0x10028c4,
    'braille_dots_1378': 0x10028c5,
    'braille_dots_2378': 0x10028c6,
    'braille_dots_12378': 0x10028c7,
    'braille_dots_478': 0x10028c8,
    'braille_dots_1478': 0x10028c9,
    'braille_dots_2478': 0x10028ca,
    'braille_dots_12478': 0x10028cb,
    'braille_dots_3478': 0x10028cc,
    'braille_dots_13478': 0x10028cd,
    'braille_dots_23478': 0x10028ce,
    'braille_dots_123478': 0x10028cf,
    'braille_dots_578': 0x10028d0,
    'braille_dots_1578': 0x10028d1,
    'braille_dots_2578': 0x10028d2,
    'braille_dots_12578': 0x10028d3,
    'braille_dots_3578': 0x10028d4,
    'braille_dots_13578': 0x10028d5,
    'braille_dots_23578': 0x10028d6,
    'braille_dots_123578': 0x10028d7,
    'braille_dots_4578': 0x10028d8,
    'braille_dots_14578': 0x10028d9,
    'braille_dots_24578': 0x10028da,
    'braille_dots_124578': 0x10028db,
    'braille_dots_34578': 0x10028dc,
    'braille_dots_134578': 0x10028dd,
    'braille_dots_234578': 0x10028de,
    'braille_dots_1234578': 0x10028df,
    'braille_dots_678': 0x10028e0,
    'braille_dots_1678': 0x10028e1,
    'braille_dots_2678': 0x10028e2,
    'braille_dots_12678': 0x10028e3,
    'braille_dots_3678': 0x10028e4,
    'braille_dots_13678': 0x10028e5,
    'braille_dots_23678': 0x10028e6,
    'braille_dots_123678': 0x10028e7,
    'braille_dots_4678': 0x10028e8,
    'braille_dots_14678': 0x10028e9,
    'braille_dots_24678': 0x10028ea,
    'braille_dots_124678': 0x10028eb,
    'braille_dots_34678': 0x10028ec,
    'braille_dots_134678': 0x10028ed,
    'braille_dots_234678': 0x10028ee,
    'braille_dots_1234678': 0x10028ef,
    'braille_dots_5678': 0x10028f0,
    'braille_dots_15678': 0x10028f1,
    'braille_dots_25678': 0x10028f2,
    'braille_dots_125678': 0x10028f3,
    'braille_dots_35678': 0x10028f4,
    'braille_dots_135678': 0x10028f5,
    'braille_dots_235678': 0x10028f6,
    'braille_dots_1235678': 0x10028f7,
    'braille_dots_45678': 0x10028f8,
    'braille_dots_145678': 0x10028f9,
    'braille_dots_245678': 0x10028fa,
    'braille_dots_1245678': 0x10028fb,
    'braille_dots_345678': 0x10028fc,
    'braille_dots_1345678': 0x10028fd,
    'braille_dots_2345678': 0x10028fe,
    'braille_dots_12345678': 0x10028ff,
    'XF86PowerOff': 0x1008ff2a,
    'XF86WakeUp': 0x1008ff2b,
    'XF86Sleep': 0x1008ff2f,
    }


# str to Namesym and int to Keysym
DEFAULT = {}
for nm, code in _KEYSYMS.iteritems():
    DEFAULT.setdefault(namesym.Namesym(nm), keysym.Keysym(code))

del _KEYSYMS, code, nm


class NameToSym(object):
    r"""Keysymdef

    Keysymdef is a object.
    Responsibility:
    """
    _map = DEFAULT.copy()
    _missing = keysym.Keysym(NoSymbol)

    @classmethod
    def getmap(cls, ):
        r"""SUMMARY

        getmap()

        @Return:

        @Error:
        """
        return cls._map

    @classmethod
    def getmissing(cls, ):
        r"""SUMMARY

        getmissing()

        @Return:

        @Error:
        """
        return cls._missing

    @classmethod
    def setmissing(cls, missing):
        r"""SUMMARY

        setmissing(missing)

        @Arguments:
        - `missing`:

        @Return:

        @Error:
        """
        cls._missing = missing

    def __repr__(self):
        return '{0.__class__.__name__}({1})'.format(self, _pformat(self._map))

    def name_to_sym(self, name):
        r"""SUMMARY

        name_to_sym(name)

        @Arguments:
        - `name`:

        @Return:

        @Error:
        """
        return self._map.get(name, self._missing)

    def __getitem__(self, key):
        return self._map.get(key, self._missing)

    def __setitem__(self, key, val):
        self._map[namesym.Namesym(key)] = keysym.Keysym(val)

    def __delitem__(self, key):
        del self._map[key]

    def clear(self, ):
        r"""SUMMARY

        clear()

        @Return:

        @Error:
        """
        self._map.clear()

    def listnames(self, ):
        r"""SUMMARY

        names()

        @Return:

        @Error:
        """
        return self._map.keys()

    def iternames(self, ):
        r"""SUMMARY

        iternames()

        @Return:

        @Error:
        """
        return self._map.iterkeys()

    def listsyms(self, ):
        r"""SUMMARY

        listsyms()

        @Return:

        @Error:
        """
        return self._map.values()

    def itersyms(self, ):
        r"""SUMMARY

        itersyms()

        @Return:

        @Error:
        """
        return self._map.itervalues()

    def items(self, ):
        r"""SUMMARY

        items()

        @Return:

        @Error:
        """
        return self._map.items()

    def iteritems(self, ):
        r"""SUMMARY

        iteritems()

        @Return:

        @Error:
        """
        return self._map.iteritems()

    def hasname(self, name):
        r"""SUMMARY

        hasname(name)

        @Arguments:
        - `name`:

        @Return:

        @Error:
        """
        return name in self._map

    def setdefault(self, name, sym):
        r"""SUMMARY

        setdefault(name, sym)

        @Arguments:
        - `name`:
        - `sym`:

        @Return:

        @Error:
        """
        return self._map.setdefault(name, sym)

    def __contains__(self, name):
        return name in self._map

    def __len__(self):
        return len(self._map)


class SymToName(object):
    r"""SymToName

    SymToName is a object.
    Responsibility:
    """
    _map = _swapdict(NameToSym.getmap())
    _missing = namesym.Namesym('')

    @classmethod
    def getmissing(cls, ):
        r"""SUMMARY

        getmissing()

        @Return:

        @Error:
        """
        return cls._missing

    @classmethod
    def setmissing(cls, missing):
        r"""SUMMARY

        setmissing(missing)

        @Arguments:
        - `missing`:

        @Return:

        @Error:
        """
        cls._missing = missing

    def sym_to_name(self, sym):
        r"""SUMMARY

        sym_to_name(sym)

        @Arguments:
        - `sym`:

        @Return:

        @Error:
        """
        return self._map.get(sym, self._missing)

    def __getitem__(self, key):
        return self._map.get(key, self._missing)

    def __setitem__(self, key, val):
        self._map[keysym.Keysym(val)] = namesym.Namesym(key)

    def __delitem__(self, key):
        del self._map[key]

    def clear(self, ):
        r"""SUMMARY

        clear()

        @Return:

        @Error:
        """
        self._map.clear()

    def listsyms(self, ):
        r"""SUMMARY

        listsyms()

        @Return:

        @Error:
        """
        return self._map.keys()

    def itersyms(self, ):
        r"""SUMMARY

        itersyms()

        @Return:

        @Error:
        """
        return self._map.iterkeys()

    def listnames(self, ):
        r"""SUMMARY

        listnames()

        @Return:

        @Error:
        """
        return self._map.values()

    def iternames(self, ):
        r"""SUMMARY

        iternames()

        @Return:

        @Error:
        """
        return self._map.itervalues()

    def items(self, ):
        r"""SUMMARY

        items()

        @Return:

        @Error:
        """
        return self._map.items()

    def iteritems(self, ):
        r"""SUMMARY

        iteritems()

        @Return:

        @Error:
        """
        return self._map.iteritems()

    def hassym(self, sym):
        r"""SUMMARY

        hasname(sym)

        @Arguments:
        - `sym`:

        @Return:

        @Error:
        """
        return sym in self._map

    def setdefault(self, sym, name):
        r"""SUMMARY

        setdefault(name, sym)

        @Arguments:
        - `name`:
        - `sym`:

        @Return:

        @Error:
        """
        return self._map.setdefault(sym, name)

    def __contains__(self, name):
        return name in self._map

    def __len__(self):
        return len(self._map)


class Keysymdef(object):
    r"""Keysymdef

    Keysymdef is a object.
    Responsibility:
    """
    _nametosym = NameToSym()
    _symtoname = SymToName()

    @classmethod
    def name_to_sym(cls, name):
        r"""SUMMARY

        name_to_sym(name)

        @Arguments:
        - `name`:

        @Return:

        @Error:
        """
        return cls._nametosym.name_to_sym(name)

    @classmethod
    def sym_to_name(cls, sym):
        r"""SUMMARY

        sym_to_name(sym)

        @Arguments:
        - `sym`:

        @Return:

        @Error:
        """
        return cls._symtoname.sym_to_name(sym)

    @classmethod
    def listnames(cls, ):
        r"""SUMMARY

        listnames()

        @Return:

        @Error:
        """
        return cls._nametosym.listnames()

    @classmethod
    def iternames(cls, ):
        r"""SUMMARY

        iternames()

        @Return:

        @Error:
        """
        return cls._nametosym.iternames()

    @classmethod
    def listsyms(cls, ):
        r"""SUMMARY

        listsyms()

        @Return:

        @Error:
        """
        return cls._symtoname.listsyms()

    @classmethod
    def itersyms(cls, ):
        r"""SUMMARY

        itersyms()

        @Return:

        @Error:
        """
        return cls._symtoname.itersyms()

    @classmethod
    def items(cls, ):
        r"""SUMMARY

        items()

        @Return:

        @Error:
        """
        return cls._nametosym.items()

    @classmethod
    def iteritems(cls, ):
        r"""SUMMARY

        iteritems()

        @Return:

        @Error:
        """
        return cls._nametosym.iteritems()

    @classmethod
    def set(cls, name, sym):
        r"""SUMMARY

        set(name, sym)

        @Arguments:
        - `name`:
        - `sym`:

        @Return:

        @Error:
        """
        cls._nametosym[name] = sym
        cls._symtoname[sym] = name

    @classmethod
    def setdefault(cls, name, sym):
        r"""SUMMARY

        setdefault(name, sym)

        @Arguments:
        - `name`:
        - `sym`:

        @Return:

        @Error:
        """
        cls._nametosym.setdefault(name, sym)
        cls._symtoname.setdefault(sym, name)


    @classmethod
    def isdefined(cls, key):
        r"""SUMMARY

        isdefined(key)

        @Arguments:
        - `key`:

        @Return:

        @Error:
        """
        return key in cls._symtoname or key in cls._nametosym


class CharToSym(object):
    r"""CharToSym

    CharToSym is a object.
    Responsibility:
    """
    _map = {}

    @classmethod
    def char_to_sym(cls, char):
        r"""SUMMARY

        char_to_sym(char)

        @Arguments:
        - `char`:

        @Return:

        @Error:
        """
        return cls._map.get(char, keysym.Keysym(NoSymbol))

    @classmethod
    def setdefault(cls, char, sym):
        r"""SUMMARY

        setdefault()

        @Return:

        @Error:
        """
        cls._map.setdefault(char, sym)

    @classmethod
    def clear(cls, ):
        r"""SUMMARY

        clear()

        @Return:

        @Error:
        """
        cls._map.clear()

    @classmethod
    def listchars(cls, ):
        r"""SUMMARY

        listchars()

        @Return:

        @Error:
        """
        return cls._map.keys()

    @classmethod
    def iterchars(cls, ):
        r"""SUMMARY

        iterchars()

        @Return:

        @Error:
        """
        return cls._map.iterkeys()

    @classmethod
    def listsyms(cls, ):
        r"""SUMMARY

        itersyms()

        @Return:

        @Error:
        """
        return cls._map.values()

    @classmethod
    def itersyms(cls, ):
        r"""SUMMARY

        itersyms()

        @Return:

        @Error:
        """
        return cls._map.itervalues()

    @classmethod
    def items(cls, ):
        r"""SUMMARY

        items()

        @Return:

        @Error:
        """
        return cls._map.items()

    @classmethod
    def iteritems(cls, ):
        r"""SUMMARY

        iteritems()

        @Return:

        @Error:
        """
        return cls._map.iteritems()

    @classmethod
    def set(cls, char, sym):
        r"""SUMMARY

        set()

        @Return:

        @Error:
        """
        cls._map[char] = sym

    def __repr__(self):
        return '{0.__class__.__name__}({1})'.format(self, _pformat(self._map))


for s in Keysymdef.itersyms():
    try:
        c = s.to_char()
    except err.ConvertError:
        continue
    CharToSym.setdefault(c, s)

del s, c



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# keysymdef.py ends here
