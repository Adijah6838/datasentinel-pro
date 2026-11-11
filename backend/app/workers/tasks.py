import time
import asyncio
import json
from app.workers.celery_app import celery_app
from app.ws.manager import manager
from app.db.session import SessionLocal
from app.models.quality_rule import QualityRule

@celery_app.task(name="ingest_data_source")
def ingest_data_task(source_id: str):
    print(f"🚀 [CELERY] Starting ingestion for data source: {source_id}")
    asyncio.run(manager.broadcast(json.dumps({"event": "ingest_start", "source_id": source_id})))
    
    # 1. Fetch the rules for this data source from the database
    db = SessionLocal()
    rules = db.query(QualityRule).filter(QualityRule.data_source_id == source_id).all()
    db.close()

    # 2. Simulate ingesting data and running the rules
    time.sleep(3) # Simulate data fetching time
    
    passed_rules = 0
    failed_rules = 0
    
    for rule in rules:
        print(f"Checking rule: {rule.name} ({rule.rule_type}) on column {rule.column_name}")
        # Simulating validation logic based on rule type
        if rule.rule_type == "completeness":
            passed_rules += 1 # Mock success
        elif rule.rule_type == "uniqueness":
            failed_rules += 1 # Mock failure
        
        time.sleep(1) # Simulate processing time per rule

    # 3. Broadcast the final results
    result_payload = {
        "event": "ingest_success", 
        "source_id": source_id,
        "rules_evaluated": len(rules),
        "rules_passed": passed_rules,
        "rules_failed": failed_rules
    }
    
    print(f"✅ [CELERY] Finished ingestion. Results: {result_payload}")
    asyncio.run(manager.broadcast(json.dumps(result_payload)))
    
    return result_payload