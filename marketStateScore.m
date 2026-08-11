function out = marketStateScore(features)
%MARKETSTATESCORE Transparent market-state baseline for research.
%   FEATURES is a timetable containing EquityReturn, RateChangeBp,
%   OilReturn, VolChange, and LiquidityZ. OUT appends Score, Regime,
%   and Confidence. This function is educational and not trading advice.

arguments
    features timetable
end

required = ["EquityReturn","RateChangeBp","OilReturn", ...
    "VolChange","LiquidityZ"];
missingVars = setdiff(required, string(features.Properties.VariableNames));
assert(isempty(missingVars), "Missing variables: %s", strjoin(missingVars, ", "));

X = features{:, required};
available = mean(~isnan(X), 2);

% Winsorize extreme inputs without using future distribution estimates.
clip = @(x, lo, hi) min(max(x, lo), hi);
eq = clip(X(:,1), -0.04, 0.04) / 0.04;
rates = clip(X(:,2), -20, 20) / 20;
oil = clip(X(:,3), -0.08, 0.08) / 0.08;
vol = clip(X(:,4), -0.25, 0.25) / 0.25;
liq = clip(X(:,5), -3, 3) / 3;

Z = [eq, rates, oil, vol, liq];
Z(isnan(Z)) = 0;

% Higher score means more stressed market state.
w = [-0.20, 0.22, 0.18, 0.28, -0.12];
score = 100 ./ (1 + exp(-3 * (Z * w')));

edges = [-inf, 25, 50, 75, inf];
labels = categorical(["Low","Moderate","High","Stressed"]);
bucket = discretize(score, edges);
regime = labels(bucket);
regime = regime(:);

distanceFromBoundary = min(abs(score - [25, 50, 75]), [], 2);
confidence = min(1, distanceFromBoundary / 20) .* available;

out = features;
out.Score = score;
out.Regime = regime;
out.Confidence = confidence;
end
