from langworld_db_data.mdlisters.listed_value_lister import ListedValueLister
from langworld_db_data.filetools.txt import read_non_empty_lines_from_txt_file
from tests.paths import DIR_WITH_TEST_FEATURE_PROFILES, DIR_WITH_VALIDATORS_TEST_FILES


def test_write_grouped_by_feature():
    lister = ListedValueLister(
        dir_with_feature_profiles=DIR_WITH_TEST_FEATURE_PROFILES,
        file_with_listed_values=DIR_WITH_VALIDATORS_TEST_FILES / 'features_listed_values_OK.csv'
    )

    output_file = DIR_WITH_VALIDATORS_TEST_FILES / 'listed_values_by_feature.md'
    gold_standard_file = DIR_WITH_VALIDATORS_TEST_FILES / 'listed_values_by_feature_sample.md'

    lister.write_grouped_by_feature(output_file=output_file)
    assert output_file.exists()

    output_lines = read_non_empty_lines_from_txt_file(output_file)
    gold_standard_lines = read_non_empty_lines_from_txt_file(gold_standard_file)

    for output_line, gold_standard_line in zip(output_lines, gold_standard_lines):
        assert output_line == gold_standard_line, \
            f"Output line {output_line} does not match gold standard line {gold_standard_line}"

    output_file.unlink()