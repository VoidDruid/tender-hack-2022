 curl -X POST "http://elastic:qwerfvcxzasd@localhost:9200/product/_delete_by_query?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match_all": {
    }
  }
}
'
