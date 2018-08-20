# NBA API

[list of all player ids](http://stats.nba.com/stats/commonallplayers?IsOnlyCurrentSeason=1&LeagueID=00&Season=2017-18)

[list of all paramaters for stats.nba API](https://github.com/kshvmdn/nba.js/blob/master/docs/api/STATS.md)

## Parameter Possible Values

\begin{itemize}
    \item Conference: null, east, west
    \item DateFrom:
    \item DateTo: 
    \item Division: null
        'Atlantic'
        'Central'
        'Northwest'
        'Pacific'
        'Southeast'
        'Southwest'
        'East'
        'West'
    \item GameScope: 'Season'
        'Yesterday'
        'Last 10'
    \item GameSegment: null
        'First Half'
        'Second Half'
        'Overtime'
    \item LastNGames: 0 n
    \item LeagueID: '00' (NBA)
        '10'
        '20'
    \item Location: null
        'Home'
        'Away'
    \item MeasureType: 'Base'
        'Advanced'
        'Misc'
        'Scoring'
        'Usage'
        'Opponent'
        'Defense'
    \item Month: '0'
        null
        0 for all, 1-12 for months of year (12=sept, 1=oct, 2=dec, etc)
    \item OpponentTeamID:
    \item Outcome: null
            'W'
            'L'
    \item PaceAdjust: ?
    \item Period: '0'
        '-13'
    \item PerMode: 'PerGame'
        'Per100Possessions'
        'Per36'
        'Per40'
        'Per48'
        'PerMinute'
        'PerPossession'
        'PerPlay'
        'MinutePer'
        'Totals'
    \item PlayerExperience: ?
    \item PlayerPosition: null
        'F'
        'C'
        'G'
    \item PlusMinus: ?
    \item PORound: ?
    \item Rank: ?
    \item Season: 'YYYY-YY', e.g. '2015-2016'
        'All Time'
    \item SeasonSegment: null
        'Pre All-Star'
        'Post All-Star'
    \item SeasonType: 'Regular Season'
        'Pre Season'
        'Playoffs'
        'All Star'
    \item ShotClockRange: null
        '24-22'
        '22-18 Very Early'
        '18-15 Early'
        '15-7 Average'
        '7-4 Late'
        '4-0 Very Late'
        'Shot Clock Off'
    \item StarterBench: null
        'Starters'
        'Bench'
    \item TeamID:
    \item VsConference: ?
    \item VsDivision ?
\end{itemize}

