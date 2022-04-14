from langworld_db_data.cldfwriters.cldf_dataset_writer import CLDFDatasetWriter
from langworld_db_data.mdlisters.custom_value_lister import CustomValueLister
from langworld_db_data.mdlisters.listed_value_lister import ListedValueLister
from langworld_db_data.validators.doculect_inventory_validator import DoculectInventoryValidator
from langworld_db_data.validators.feature_profile_validator import FeatureProfileValidator
from langworld_db_data.validators.feature_value_inventory_validator import FeatureValueInventoryValidator


def main():
    # These will also run during testing, but it doesn't hurt to check again
    DoculectInventoryValidator().validate()
    FeatureValueInventoryValidator().validate()
    # Strict mode triggers exception if value name does not match value name in an inventory for given value ID.
    # Since value name in feature profile is only there for readability, I could disable strict mode
    # at later stages of the project (when I am sure that a mismatch can only be caused by planned renaming
    # of a value  in the inventory).
    FeatureProfileValidator(strict_mode=True).validate()

    print('\nWriting Markdown files')
    CustomValueLister().write_grouped_by_feature()
    CustomValueLister().write_grouped_by_volume_and_doculect()
    ListedValueLister().write_grouped_by_feature()

    print('\nWriting CLDF')
    CLDFDatasetWriter().write()


if __name__ == '__main__':
    main()
