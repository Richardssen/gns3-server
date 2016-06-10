#!/usr/bin/env python
#
# Copyright (C) 2016 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import asyncio
from unittest.mock import MagicMock


from gns3server.utils.file_watcher import FileWatcher


def test_file_watcher(async_run, tmpdir):
    file = tmpdir / "test"
    file.write("a")
    callback = MagicMock()
    fw = FileWatcher(file, callback, delay=0.5)
    async_run(asyncio.sleep(1))
    assert not callback.called
    file.write("b")
    async_run(asyncio.sleep(1.5))
    callback.assert_called_with(str(file))


def test_file_watcher_not_existing(async_run, tmpdir):
    file = tmpdir / "test"
    callback = MagicMock()
    fw = FileWatcher(file, callback, delay=0.5)
    async_run(asyncio.sleep(1))
    assert not callback.called
    file.write("b")
    async_run(asyncio.sleep(1.5))
    callback.assert_called_with(str(file))

