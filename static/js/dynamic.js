// example toop song list
const top_song_list = [
  {
    song_title: "Babaero",
    song_artists: "gins&melodies, Hev Abi",
    curr_rank: 1,
    prev_rank: 2,
    cover_art_url:
      "https://i.scdn.co/image/ab67616d0000b2734d5b5fd52ad1196eb5306665",
  },
  {
    song_title: "we can't be friends (wait for your love)",
    song_artists: "Ariana Grande",
    curr_rank: 2,
    prev_rank: 1,
    cover_art_url:
      "https://i.scdn.co/image/ab67616d0000b273bd3de668e4784d791c4ab695",
  },
  {
    song_title: "Alam Mo Ba Girl",
    song_artists: "Hev Abi",
    curr_rank: 3,
    prev_rank: 4,
    cover_art_url:
      "https://i.scdn.co/image/ab67616d0000b2737300c1e7edcdbd15a42e1579",
  },
  {
    song_title: "End of Beginning",
    song_artists: "Djo",
    curr_rank: 4,
    prev_rank: 3,
    cover_art_url:
      "https://i.scdn.co/image/ab67616d0000b273fddfffec51b4580acae727c1",
  },
  {
    song_title: "Walang Alam",
    song_artists: "Hev Abi",
    curr_rank: 5,
    prev_rank: 5,
    cover_art_url:
      "https://i.scdn.co/image/ab67616d0000b2737300c1e7edcdbd15a42e1579",
  },
  {
    song_title: "intro (end of the world)",
    song_artists: "Ariana Grande",
    curr_rank: 6,
    prev_rank: 6,
  },
  {
    song_title: "Makasarili Malambing (feat. Hev Abi)",
    song_artists: "Kristina Dawn, Hev Abi",
    curr_rank: 7,
    prev_rank: 8,
  },
  {
    song_title: "TAKE ALL THE LOVE",
    song_artists: "Arthur Nery",
    curr_rank: 8,
    prev_rank: 9,
  },
  {
    song_title: "Sumugal",
    song_artists: "Hev Abi, Unotheone, LK",
    curr_rank: 9,
    prev_rank: 7,
  },
  {
    song_title: "Marikit Sa Dilim",
    song_artists: "Juan Caoile, Kyleswish, Jawz",
    curr_rank: 10,
    prev_rank: 11,
  },
];

let len = top_song_list.length;

function addTopOne() {
  const topOneContainer = document.getElementById("top-1-song-container");
  let i = 0;

  let songDataWrapper = document.createElement("div");
  songDataWrapper.className = "song-data__wrapper";

  let songCoverArtContainer = document.createElement("div");
  songCoverArtContainer.className = "song-cover-art__container";

  let coverArt = document.createElement("img");
  coverArt.src = top_song_list[i]["cover_art_url"];

  let songInfoWrapper = document.createElement("div");
  songInfoWrapper.className = "song-info__wrapper";

  let songInfoDetailsWrapper = document.createElement("div");
  songInfoDetailsWrapper.className = "song-info-details__wrapper";

  let songTitle = document.createElement("p");
  songTitle.className = "song-title";
  songTitle.textContent = top_song_list[i]["song_title"];

  let songArtists = document.createElement("p");
  songArtists.className = "song-artists";
  songArtists.textContent = top_song_list[i]["song_artists"];

  let prevRank = document.createElement("p");
  prevRank.className = "prev-rank";
  prevRank.textContent = "Last week: " + String(top_song_list[i]["prev_rank"]);

  let currRank = document.createElement("p");
  currRank.className = "curr-rank";
  currRank.textContent = "Current: " + String(top_song_list[i]["curr_rank"]);

  // Build element hierarchy
  // song-info-details__wrapper
  songInfoDetailsWrapper.append(songTitle);
  songInfoDetailsWrapper.append(songArtists);

  // song-info__wrapper
  songInfoWrapper.append(songInfoDetailsWrapper);
  songInfoWrapper.append(currRank);
  songInfoWrapper.append(prevRank);

  songCoverArtContainer.append(coverArt);

  songDataWrapper.append(songCoverArtContainer);
  songDataWrapper.append(songInfoWrapper);

  topOneContainer.append(songDataWrapper);
}

function addTopFive() {
  const topFiveContainer = document.getElementById("top-5-songs-container");

  for (let i = 1; i < 5; i++) {
    console.log("Adding top song no. ", i + 1);
    let songDataWrapper = document.createElement("div");
    songDataWrapper.className = "song-data__wrapper";

    let songCoverArtContainer = document.createElement("div");
    songCoverArtContainer.className = "song-cover-art__container";

    let coverArt = document.createElement("img");
    coverArt.src = top_song_list[i]["cover_art_url"];

    let songInfoWrapper = document.createElement("div");
    songInfoWrapper.className = "song-info__wrapper";

    let songInfoDetailsWrapper = document.createElement("div");
    songInfoDetailsWrapper.className = "song-info-details__wrapper";

    let songTitle = document.createElement("p");
    songTitle.className = "song-title";
    songTitle.textContent = top_song_list[i]["song_title"];

    let songArtists = document.createElement("p");
    songArtists.className = "song-artists";
    songArtists.textContent = top_song_list[i]["song_artists"];

    let prevRank = document.createElement("p");
    prevRank.className = "prev-rank";
    prevRank.textContent =
      "Last week: " + String(top_song_list[i]["prev_rank"]);

    let currRank = document.createElement("p");
    currRank.className = "curr-rank";
    currRank.textContent = "Current: " + String(top_song_list[i]["curr_rank"]);

    // Build element hierarchy
    // song-info-details__wrapper
    songInfoDetailsWrapper.append(songTitle);
    songInfoDetailsWrapper.append(songArtists);

    // song-info__wrapper
    songInfoWrapper.append(songInfoDetailsWrapper);

    songCoverArtContainer.append(coverArt);
    songCoverArtContainer.append(currRank);
    songCoverArtContainer.append(prevRank);

    songDataWrapper.append(songCoverArtContainer);
    songDataWrapper.append(songInfoWrapper);

    topFiveContainer.append(songDataWrapper);
  }
}

function addTopTen() {
  const topTenContainer = document.getElementById("top-10-songs-container");

  for (let i = 5; i < len; i++) {
    let songDataWrapper = document.createElement("div");
    songDataWrapper.className = "song-data__wrapper";

    let songTitle = document.createElement("p");
    songTitle.className = "song-title";
    songTitle.textContent = top_song_list[i]["song_title"];

    let songArtists = document.createElement("p");
    songArtists.className = "song-artists";
    songArtists.textContent = top_song_list[i]["song_artists"];

    let prevRank = document.createElement("p");
    prevRank.className = "prev-rank";
    prevRank.textContent =
      "Last week: " + String(top_song_list[i]["prev_rank"]);

    let currRank = document.createElement("p");
    currRank.className = "curr-rank";
    currRank.textContent = String(top_song_list[i]["curr_rank"]);

    songDataWrapper.append(currRank);
    songDataWrapper.append(songTitle);
    songDataWrapper.append(songArtists);
    songDataWrapper.append(prevRank);

    topTenContainer.append(songDataWrapper);
  }
}

addTopOne();
addTopFive();
addTopTen();
