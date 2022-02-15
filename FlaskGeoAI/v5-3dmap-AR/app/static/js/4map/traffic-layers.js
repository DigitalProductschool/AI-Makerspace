var trafficLayers = [{
  "id": "traffic-0-other-high-case",
  "type": "line",
  "source": "trafficSource",
  "source-layer": "traffic",
  "minzoom": 16,
  "filter": [
    "all",
    [
      "==",
      "$type",
      "LineString"
    ],
    [
      "all",
      [
        "==",
        "class",
        "street"
      ],
      [
        "==",
        "congestion",
        "low"
      ]
    ]
  ],
  "layout": {
    "line-join": "round",
    "visibility": "visible"
  },
  "paint": {
    "line-blur": 0,
    "line-color": "#fff",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          7,
          0.3
        ],
        [
          18,
          6
        ],
        [
          22,
          100
        ]
      ]
    },
    "line-opacity": 1,
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          11,
          1.25
        ],
        [
          14,
          2.5
        ],
        [
          17,
          5.5
        ],
        [
          22,
          34
        ]
      ]
    }
  }
},
{
  "id": "traffic-0-other-high",
  "type": "line",
  "source": "trafficSource",
  "source-layer": "traffic",
  "layout": {
    "visibility": "visible"
  },
  "paint": {
    "line-blur": 0,
    "line-color": "hsl(100, 70%, 45%)",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          7,
          0.3
        ],
        [
          18,
          6
        ],
        [
          22,
          100
        ]
      ]
    },
    "line-opacity": 1,
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          11,
          1
        ],
        [
          14,
          2
        ],
        [
          17,
          4
        ],
        [
          22,
          30
        ]
      ]
    }
  },
  "filter": [
    "all",
    [
      "==",
      "$type",
      "LineString"
    ],
    [
      "all",
      [
        "==",
        "class",
        "street"
      ],
      [
        "==",
        "congestion",
        "low"
      ]
    ]
  ]
},
{
  "id": "traffic-0-other-case",
  "type": "line",
  "source": "trafficSource",
  "source-layer": "traffic",
  "minzoom": 5,
  "filter": [
        "all",
        [
          "==",
          "$type",
          "LineString"
        ],
        [
          "all",
          [
            "!in",
            "class",
            "motorway",
            "motorway_link",
            "service",
            "street",
            "trunk"
          ],
          [
            "==",
            "congestion",
            "low"
          ]
        ]
      ],
  "layout": {
    "line-join": "round",
    "visibility": "visible"
  },
  "paint": {
    "line-blur": 0,
    "line-color": "#fff",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          7,
          0.3
        ],
        [
          18,
          6
        ],
        [
          22,
          100
        ]
      ]
    },
    "line-opacity": 1,
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          11,
          1.25
        ],
        [
          14,
          2.5
        ],
        [
          17,
          5.5
        ],
        [
          22,
          34
        ]
      ]
    }
  },
  "filter": [
    "all",
    [
      "==",
      "$type",
      "LineString"
    ],
    [
      "all",
      [
        "==",
        "class",
        "street"
      ],
      [
        "==",
        "congestion",
        "low"
      ]
    ]
  ]
},
{
  "id": "traffic-0-other",
  "type": "line",
  "source": "trafficSource",
  "source-layer": "traffic",
  "layout": {
    "visibility": "visible"
  },
  "paint": {
    "line-blur": 0,
    "line-color": "hsl(100, 70%, 45%)",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          7,
          0.3
        ],
        [
          18,
          6
        ],
        [
          22,
          100
        ]
      ]
    },
    "line-opacity": 1,
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          11,
          1
        ],
        [
          14,
          2
        ],
        [
          17,
          4
        ],
        [
          22,
          30
        ]
      ]
    }
  },
  "filter": [
        "all",
        [
          "==",
          "$type",
          "LineString"
        ],
        [
          "all",
          [
            "!in",
            "class",
            "motorway",
            "motorway_link",
            "service",
            "street",
            "trunk"
          ],
          [
            "==",
            "congestion",
            "low"
          ]
        ]
      ]
},
{
  "id": "traffic-1-other-high-case",
  "type": "line",
  "source": "trafficSource",
  "source-layer": "traffic",
  "minzoom": 16,
  "filter": [
    "all",
    [
      "==",
      "$type",
      "LineString"
    ],
    [
      "all",
      [
        "==",
        "class",
        "street"
      ],
      [
        "==",
        "congestion",
        "moderate"
      ]
    ]
  ],
  "layout": {
    "line-join": "round",
    "visibility": "visible"
  },
  "paint": {
    "line-blur": 0,
    "line-color": "#fff",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          7,
          0.3
        ],
        [
          18,
          6
        ],
        [
          22,
          100
        ]
      ]
    },
    "line-opacity": 1,
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          11,
          1.25
        ],
        [
          14,
          2.5
        ],
        [
          17,
          5.5
        ],
        [
          22,
          34
        ]
      ]
    }
  }
},
{
  "id": "traffic-1-other-high",
  "type": "line",
  "source": "trafficSource",
  "source-layer": "traffic",
  "filter": [
    "all",
    [
      "==",
      "$type",
      "LineString"
    ],
    [
      "all",
      [
        "==",
        "class",
        "street"
      ],
      [
        "==",
        "congestion",
        "moderate"
      ]
    ]
  ],
  "layout": {
    "visibility": "visible"
  },
  "paint": {
    "line-blur": 0,
    "line-color": "hsl(45, 90%, 50%)",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          7,
          0.3
        ],
        [
          18,
          6
        ],
        [
          22,
          100
        ]
      ]
    },
    "line-opacity": 1,
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          11,
          1
        ],
        [
          14,
          2
        ],
        [
          17,
          4
        ],
        [
          22,
          30
        ]
      ]
    }
  }
},
{
  "id": "traffic-1-other-case",
  "type": "line",
  "source": "trafficSource",
  "source-layer": "traffic",
  "minzoom": 5,
  "filter": [
    "all",
    [
      "==",
      "$type",
      "LineString"
    ],
    [
      "all",
      [
        "!in",
        "class",
        "motorway",
        "motorway_link",
        "service",
        "street",
        "trunk"
      ],
      [
        "==",
        "congestion",
        "moderate"
      ]
    ]
  ],
  "layout": {
    "line-join": "round",
    "visibility": "visible"
  },
  "paint": {
    "line-blur": 0,
    "line-color": "#fff",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          7,
          0.3
        ],
        [
          18,
          6
        ],
        [
          22,
          100
        ]
      ]
    },
    "line-opacity": 1,
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          11,
          1.25
        ],
        [
          14,
          2.5
        ],
        [
          17,
          5.5
        ],
        [
          22,
          34
        ]
      ]
    }
  }
},
{
  "id": "traffic-1-other",
  "type": "line",
  "source": "trafficSource",
  "source-layer": "traffic",
  "layout": {
    "visibility": "visible"
  },
  "filter": [
        "all",
        [
          "==",
          "$type",
          "LineString"
        ],
        [
          "all",
          [
            "!in",
            "class",
            "motorway",
            "motorway_link",
            "service",
            "street",
            "trunk"
          ],
          [
            "==",
            "congestion",
            "moderate"
          ]
        ]
      ],
  "paint": {
    "line-blur": 0,
    "line-color": "hsl(45, 90%, 50%)",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          7,
          0.3
        ],
        [
          18,
          6
        ],
        [
          22,
          100
        ]
      ]
    },
    "line-opacity": 1,
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          11,
          1
        ],
        [
          14,
          2
        ],
        [
          17,
          4
        ],
        [
          22,
          30
        ]
      ]
    }
  }
},
{
  "id": "traffic-2-other-high-case",
  "type": "line",
  "source": "trafficSource",
  "source-layer": "traffic",
  "minzoom": 16,
  "filter": [
    "all",
    [
      "==",
      "$type",
      "LineString"
    ],
    [
      "all",
      [
        "==",
        "class",
        "street"
      ],
      [
        "==",
        "congestion",
        "heavy"
      ]
    ]
  ],
  "layout": {
    "line-join": "round",
    "visibility": "visible"
  },
  "paint": {
    "line-blur": 0,
    "line-color": "#fff",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          7,
          0.3
        ],
        [
          18,
          6
        ],
        [
          22,
          100
        ]
      ]
    },
    "line-opacity": 1,
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          11,
          1.25
        ],
        [
          14,
          2.5
        ],
        [
          17,
          5.5
        ],
        [
          22,
          34
        ]
      ]
    }
  }
},
{
  "id": "traffic-2-other-high",
  "type": "line",
  "source": "trafficSource",
  "source-layer": "traffic",
  "layout": {
    "visibility": "visible"
  },
  "filter": [
    "all",
    [
      "==",
      "$type",
      "LineString"
    ],
    [
      "all",
      [
        "==",
        "class",
        "street"
      ],
      [
        "==",
        "congestion",
        "heavy"
      ]
    ]
  ],
  "paint": {
    "line-blur": 0,
    "line-color": "hsl(30, 90%, 50%)",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          7,
          0.3
        ],
        [
          18,
          6
        ],
        [
          22,
          100
        ]
      ]
    },
    "line-opacity": 1,
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          11,
          1
        ],
        [
          14,
          2
        ],
        [
          17,
          4
        ],
        [
          22,
          30
        ]
      ]
    }
  }
},
{
  "id": "traffic-2-other-case",
  "type": "line",
  "source": "trafficSource",
  "source-layer": "traffic",
  "minzoom": 5,
  "filter": [
        "all",
        [
          "==",
          "$type",
          "LineString"
        ],
        [
          "all",
          [
            "!in",
            "class",
            "motorway",
            "motorway_link",
            "service",
            "street",
            "trunk"
          ],
          [
            "==",
            "congestion",
            "heavy"
          ]
        ]
      ],
  "layout": {
    "line-join": "round",
    "visibility": "visible"
  },
  "paint": {
    "line-blur": 0,
    "line-color": "#fff",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          7,
          0.3
        ],
        [
          18,
          6
        ],
        [
          22,
          100
        ]
      ]
    },
    "line-opacity": 1,
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          11,
          1.25
        ],
        [
          14,
          2.5
        ],
        [
          17,
          5.5
        ],
        [
          22,
          34
        ]
      ]
    }
  }
},
{
  "id": "traffic-2-other",
  "type": "line",
  "source": "trafficSource",
  "source-layer": "traffic",
  "filter": [
        "all",
        [
          "==",
          "$type",
          "LineString"
        ],
        [
          "all",
          [
            "!in",
            "class",
            "motorway",
            "motorway_link",
            "service",
            "street",
            "trunk"
          ],
          [
            "==",
            "congestion",
            "heavy"
          ]
        ]
      ],
  "layout": {
    "visibility": "visible"
  },
  "paint": {
    "line-blur": 0,
    "line-color": "hsl(30, 90%, 50%)",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          7,
          0.3
        ],
        [
          18,
          6
        ],
        [
          22,
          100
        ]
      ]
    },
    "line-opacity": 1,
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          11,
          1
        ],
        [
          14,
          2
        ],
        [
          17,
          4
        ],
        [
          22,
          30
        ]
      ]
    }
  }
},
{
  "id": "traffic-3-other-high-case",
  "type": "line",
  "source": "trafficSource",
  "source-layer": "traffic",
  "minzoom": 16,
  "filter": [
    "all",
    [
      "==",
      "$type",
      "LineString"
    ],
    [
      "all",
      [
        "==",
        "class",
        "street"
      ],
      [
        "==",
        "congestion",
        "severe"
      ]
    ]
  ],
  "layout": {
    "line-join": "round",
    "visibility": "visible"
  },
  "paint": {
    "line-blur": 0,
    "line-color": "#fff",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          7,
          0.3
        ],
        [
          18,
          6
        ],
        [
          22,
          100
        ]
      ]
    },
    "line-opacity": 1,
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          11,
          1.25
        ],
        [
          14,
          2.5
        ],
        [
          17,
          5.5
        ],
        [
          22,
          34
        ]
      ]
    }
  }
},
{
  "id": "traffic-3-other-high",
  "type": "line",
  "source": "trafficSource",
  "source-layer": "traffic",
  "layout": {
    "visibility": "visible"
  },
  "filter": [
    "all",
    [
      "==",
      "$type",
      "LineString"
    ],
    [
      "all",
      [
        "==",
        "class",
        "street"
      ],
      [
        "==",
        "congestion",
        "severe"
      ]
    ]
  ],
  "paint": {
    "line-blur": 0,
    "line-color": "hsl(0, 100%, 40%)",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          7,
          0.3
        ],
        [
          18,
          6
        ],
        [
          22,
          100
        ]
      ]
    },
    "line-opacity": 1,
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          11,
          1
        ],
        [
          14,
          2
        ],
        [
          17,
          4
        ],
        [
          22,
          30
        ]
      ]
    }
  }
},
{
  "id": "traffic-3-other-case",
  "type": "line",
  "source": "trafficSource",
  "source-layer": "traffic",
  "minzoom": 5,
  "filter": [
    "all",
    [
      "==",
      "$type",
      "LineString"
    ],
    [
      "all",
      [
        "!in",
        "class",
        "motorway",
        "motorway_link",
        "service",
        "street",
        "trunk"
      ],
      [
        "==",
        "congestion",
        "severe"
      ]
    ]
  ],
  "layout": {
    "line-join": "round",
    "visibility": "visible"
  },
  "paint": {
    "line-blur": 0,
    "line-color": "#fff",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          7,
          0.3
        ],
        [
          18,
          6
        ],
        [
          22,
          100
        ]
      ]
    },
    "line-opacity": 1,
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          11,
          1.25
        ],
        [
          14,
          2.5
        ],
        [
          17,
          5.5
        ],
        [
          22,
          34
        ]
      ]
    }
  }
},
{
  "id": "traffic-3-other",
  "type": "line",
  "source": "trafficSource",
  "layout": {
    "visibility": "visible"
  },
  "source-layer": "traffic",
  "filter": [
    "all",
    [
      "==",
      "$type",
      "LineString"
    ],
    [
      "all",
      [
        "==",
        "class",
        "street"
      ],
      [
        "==",
        "congestion",
        "severe"
      ]
    ]
  ],
  "paint": {
    "line-blur": 0,
    "line-color": "hsl(0, 100%, 40%)",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          7,
          0.3
        ],
        [
          18,
          6
        ],
        [
          22,
          100
        ]
      ]
    },
    "line-opacity": 1,
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          11,
          1
        ],
        [
          14,
          2
        ],
        [
          17,
          4
        ],
        [
          22,
          30
        ]
      ]
    }
  }
},
{
  "id": "traffic-0-motorway-case",
  "type": "line",
  "source": "trafficSource",
  "source-layer": "traffic",
  "minzoom": 5,
  "filter": [
    "all",
    [
      "==",
      "$type",
      "LineString"
    ],
    [
      "all",
      [
        "in",
        "class",
        "motorway",
        "motorway_link",
        "trunk"
      ],
      [
        "==",
        "congestion",
        "low"
      ]
    ]
  ],
  "layout": {
    "line-join": "round",
    "visibility": "visible"
  },
  "paint": {
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          7,
          3
        ],
        [
          18,
          30
        ]
      ]
    },
    "line-color": "#fff",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          5,
          0.5
        ],
        [
          13,
          3
        ],
        [
          18,
          10
        ]
      ]
    },
    "line-opacity": 1,
    "line-translate": [
      0,
      0
    ],
    "line-translate-anchor": "map",
    "line-blur": 0
  }
},
{
  "id": "traffic-0-motorway",
  "type": "line",
  "source": "trafficSource",
  "layout": {
    "visibility": "visible"
  },
  "source-layer": "traffic",
  "filter": [
    "all",
    [
      "==",
      "$type",
      "LineString"
    ],
    [
      "all",
      [
        "in",
        "class",
        "motorway",
        "motorway_link",
        "trunk"
      ],
      [
        "==",
        "congestion",
        "low"
      ]
    ]
  ],
  "paint": {
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          7,
          1.5
        ],
        [
          18,
          24
        ]
      ]
    },
    "line-color": "hsl(100, 70%, 45%)",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          5,
          0.5
        ],
        [
          13,
          3
        ],
        [
          18,
          10
        ]
      ]
    },
    "line-opacity": 1,
    "line-translate": [
      0,
      0
    ],
    "line-translate-anchor": "map",
    "line-blur": 0
  }
},
{
  "id": "traffic-1-motorway-case",
  "type": "line",
  "source": "trafficSource",
  "source-layer": "traffic",
  "minzoom": 5,
  "filter": [
    "all",
    [
      "==",
      "$type",
      "LineString"
    ],
    [
      "all",
      [
        "in",
        "class",
        "motorway",
        "motorway_link",
        "trunk"
      ],
      [
        "==",
        "congestion",
        "moderate"
      ]
    ]
  ],
  "layout": {
    "line-join": "round",
    "visibility": "visible"
  },
  "paint": {
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          7,
          3
        ],
        [
          18,
          30
        ]
      ]
    },
    "line-color": "#fff",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          5,
          0.5
        ],
        [
          13,
          3
        ],
        [
          18,
          10
        ]
      ]
    },
    "line-opacity": 1,
    "line-translate": [
      0,
      0
    ],
    "line-translate-anchor": "map",
    "line-blur": 0
  }
},
{
  "id": "traffic-1-motorway",
  "type": "line",
  "source": "trafficSource",
  "layout": {
    "visibility": "visible"
  },
  "source-layer": "traffic",
  "filter": [
    "all",
    [
      "==",
      "$type",
      "LineString"
    ],
    [
      "all",
      [
        "in",
        "class",
        "motorway",
        "motorway_link",
        "trunk"
      ],
      [
        "==",
        "congestion",
        "moderate"
      ]
    ]
  ],
  "paint": {
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          7,
          1.5
        ],
        [
          18,
          24
        ]
      ]
    },
    "line-color": "hsl(45, 90%, 50%)",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          5,
          0.5
        ],
        [
          13,
          3
        ],
        [
          18,
          10
        ]
      ]
    },
    "line-opacity": 1,
    "line-translate": [
      0,
      0
    ],
    "line-translate-anchor": "map",
    "line-blur": 0
  }
},
{
  "id": "traffic-2-motorway-case",
  "type": "line",
  "source": "trafficSource",
  "source-layer": "traffic",
  "minzoom": 5,
  "filter": [
    "all",
    [
      "==",
      "$type",
      "LineString"
    ],
    [
      "all",
      [
        "in",
        "class",
        "motorway",
        "motorway_link",
        "trunk"
      ],
      [
        "==",
        "congestion",
        "heavy"
      ]
    ]
  ],
  "layout": {
    "line-join": "round",
    "visibility": "visible"
  },
  "paint": {
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          7,
          3
        ],
        [
          18,
          30
        ]
      ]
    },
    "line-color": "#fff",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          5,
          0.5
        ],
        [
          13,
          3
        ],
        [
          18,
          10
        ]
      ]
    },
    "line-opacity": 1,
    "line-translate": [
      0,
      0
    ],
    "line-translate-anchor": "map",
    "line-blur": 0
  }
},
{
  "id": "traffic-2-motorway",
  "type": "line",
  "source": "trafficSource",
  "layout": {
    "visibility": "visible"
  },
  "source-layer": "traffic",
  "filter": [
    "all",
    [
      "==",
      "$type",
      "LineString"
    ],
    [
      "all",
      [
        "in",
        "class",
        "motorway",
        "motorway_link",
        "trunk"
      ],
      [
        "==",
        "congestion",
        "heavy"
      ]
    ]
  ],
  "paint": {
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          7,
          1.5
        ],
        [
          18,
          24
        ]
      ]
    },
    "line-color": "hsl(30, 90%, 50%)",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          5,
          0.5
        ],
        [
          13,
          3
        ],
        [
          18,
          10
        ]
      ]
    },
    "line-opacity": 1,
    "line-translate": [
      0,
      0
    ],
    "line-translate-anchor": "map",
    "line-blur": 0
  }
},
{
  "id": "traffic-3-motorway-case",
  "type": "line",
  "source": "trafficSource",
  "source-layer": "traffic",
  "minzoom": 5,
  "filter": [
    "all",
    [
      "==",
      "$type",
      "LineString"
    ],
    [
      "all",
      [
        "in",
        "class",
        "motorway",
        "motorway_link",
        "trunk"
      ],
      [
        "==",
        "congestion",
        "severe"
      ]
    ]
  ],
  "layout": {
    "line-join": "round",
    "visibility": "visible"
  },
  "paint": {
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          7,
          3
        ],
        [
          18,
          30
        ]
      ]
    },
    "line-color": "#fff",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          5,
          0.5
        ],
        [
          13,
          3
        ],
        [
          18,
          10
        ]
      ]
    },
    "line-opacity": 1,
    "line-translate": [
      0,
      0
    ],
    "line-translate-anchor": "map",
    "line-blur": 0
  }
},
{
  "id": "traffic-3-motorway",
  "type": "line",
  "source": "trafficSource",
  "layout": {
    "visibility": "visible"
  },
  "source-layer": "traffic",
  "filter": [
    "all",
    [
      "==",
      "$type",
      "LineString"
    ],
    [
      "all",
      [
        "in",
        "class",
        "motorway",
        "motorway_link",
        "trunk"
      ],
      [
        "==",
        "congestion",
        "severe"
      ]
    ]
  ],
  "paint": {
    "line-width": {
      "base": 1.5,
      "stops": [
        [
          7,
          1.5
        ],
        [
          18,
          24
        ]
      ]
    },
    "line-color": "hsl(0, 100%, 40%)",
    "line-offset": {
      "base": 1.5,
      "stops": [
        [
          5,
          0.5
        ],
        [
          13,
          3
        ],
        [
          18,
          10
        ]
      ]
    },
    "line-opacity": 1,
    "line-translate": [
      0,
      0
    ],
    "line-translate-anchor": "map",
    "line-blur": 0
  }
}];



// const toggleableLayerIds2 = ['traffic-0-other-high-case', 'traffic-0-other-high', 'traffic-0-other-case', 'traffic-0-other', 'traffic-1-other-high-case', 'traffic-1-other-high', 'traffic-1-other-case', 'traffic-1-other', 'traffic-2-other-high-case', 'traffic-2-other-high', 'traffic-2-other-case', 'traffic-2-other', 'traffic-3-other-high-case', 'traffic-3-other-high', 'traffic-3-other-case', 'traffic-3-other', 'traffic-0-motorway-case', 'traffic-0-motorway', 'traffic-1-motorway-case', 'traffic-1-motorway', 'traffic-2-motorway-case', 'traffic-2-motorway', 'traffic-3-motorway-case', 'traffic-3-motorway'];