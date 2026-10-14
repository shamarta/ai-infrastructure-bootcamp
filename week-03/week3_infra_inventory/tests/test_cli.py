from infra_inventory.cli import main


def test_demo_report_runs_and_succeeds(capsys):
    assert main([]) == 0
    out = capsys.readouterr().out
    assert "Total nodes: 3" in out
    assert "Skipped 2 invalid record(s)" in out
    assert "['node-3']" in out


def test_threshold_flag_changes_result(capsys):
    main(["--threshold", "40"])
    out = capsys.readouterr().out
    assert "node-1" in out and "node-3" in out


def test_missing_file_returns_error_code(capsys):
    assert main(["--file", "/definitely/not/here.json"]) == 1
    assert "Cannot read" in capsys.readouterr().err


def test_invalid_json_file_returns_error_code(tmp_path, capsys):
    bad = tmp_path / "bad.json"
    bad.write_text("{oops")
    assert main(["--file", str(bad)]) == 1
    assert "Invalid JSON" in capsys.readouterr().err


def test_valid_json_file_is_loaded(tmp_path, capsys):
    good = tmp_path / "nodes.json"
    good.write_text('[{"id": "x", "status": "active", "cpu_usage": 10}]')
    assert main(["--file", str(good)]) == 0
    assert "Total nodes: 1" in capsys.readouterr().out