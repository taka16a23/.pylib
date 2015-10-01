#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""keysym -- DESCRIPTION

"""
from wxcb import NoSymbol
from userint import UserInt


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


class Keysym(UserInt):
    r"""Keysym

    Keysym is a UserInt.
    Responsibility:
    """

    def isspecial(self, ):
        r"""SUMMARY

        isspecial()

        @Return:

        @Error:
        """
        return self._value in (0, 0x00ffffff)

    def islatin1(self, ):
        r"""SUMMARY

        islatin1()

        @Return:

        @Error:
        """
        return (0x0020 <= self._value <= 0x007e or
                0x00a0 <= self._value <= 0x00ff)

    def isnosymbol(self, ):
        r"""SUMMARY

        isnosymbol()

        @Return:

        @Error:
        """
        return self._value == NoSymbol

    def isunicode(self, ):
        r"""SUMMARY

        isunicode()

        @Return:

        @Error:
        """
        return 0x01000100 <= self._value <= 0x0110ffff

    def islegacy(self, ):
        r"""SUMMARY

        islegacy()

        @Return:

        @Error:
        """
        return self._value in LEGACY

    def to_char(self, ):
        r"""SUMMARY

        to_char()

        @Return:

        @Error:
        """
        if self.isspecial():
            # TODO: (Atami) [2015/01/09]
            raise StandardError()
        if self.islatin1():
            return unichr(self._value)
        if self.isunicode():
            return unichr(self - 0x01000000)
        if self.islegacy():
            return unichr(LEGACY[self._value])
        # nothing
        # TODO: (Atami) [2015/01/09]
        raise StandardError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# keysym.py ends here
