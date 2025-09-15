

import os
from textSummarizer.entity import DataValidationConfig


class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config

# This component validates that all required files exist and saves the validation status in status.txt for other stages to read it. 
# here the logic in the tutorial was incorrect, so i fixed it.
# in the original method, the valudation status value is set to False, and whenever a required file is found it's set to true
# so if a file is missing -> status: False, and then another one exists -> status: true, then status will be set to True even though not all files exist.
    def validate_all_files_exist(self) -> bool:
        try:
            # Assume valid unless proven otherwise
            validation_status = True  

            # List all files actually present
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

            # Check each required file
            for required in self.config.ALL_REQUIRED_FILES:
                if required not in all_files:
                    validation_status = False
                    break  # no need to keep checking if one is missing

            # Write status once
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e
