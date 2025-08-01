$vars = @{
  "ENVIRONMENT" = "production"
  "DEBUG" = "False"
  "ACTIVE_DB" = "railway"
  "RAILWAY_DATABASE_URL" = "postgresql://postgres:QHWefIcrwLtfnkVNxpHdzvTnzGzsFwjo@switchback.proxy.rlwy.net:17277/railway"
  "DATABASE_URL" = "postgresql://postgres:QHWefIcrwLtfnkVNxpHdzvTnzGzsFwjo@switchback.proxy.rlwy.net:17277/railway"
  "SECRET_KEY" = "pK179z2QQzIyIVge415C0e7kvdIX6p4y9d7_AQ1HTcU_hh35U4dO5guT0eKTSgj5IunErK1byXqUz5O5ysh6cQ"
  "ALGORITHM" = "HS256"
  "ACCESS_TOKEN_EXPIRE_MINUTES" = "60"
  # Ongeza zingine hapa
}

foreach ($key in $vars.Keys) {
  railway variables set "$key=$($vars[$key])"
}
