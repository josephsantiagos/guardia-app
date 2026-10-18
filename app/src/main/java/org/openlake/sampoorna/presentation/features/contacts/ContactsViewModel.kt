package org.openlake.sampoorna.presentation.features.contacts

import androidx.lifecycle.LiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.map
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import org.openlake.sampoorna.data.di.Transformer
import org.openlake.sampoorna.data.repository.ContactsRepository
import org.openlake.sampoorna.data.sources.entities.Contact
import javax.inject.Inject

@HiltViewModel
class ContactsViewModel @Inject constructor(private val repository: ContactsRepository) : ViewModel() {

    var allContacts: LiveData<List<Contact>> = repository.fetchAllContacts().map { list ->
        list.map {
            Transformer.convertContactEntityToContactModel(it)
        }
    }

    fun deleteContact(contact: Contact) = viewModelScope.launch(Dispatchers.IO) {
        repository.delete(contact)
    }

    fun insertContact(contact: Contact) = viewModelScope.launch(Dispatchers.IO) {
        repository.insert(contact)
    }

}